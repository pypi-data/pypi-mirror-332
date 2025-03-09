import time
import logging
import random
import gc
import weakref
import asyncio
from typing import Dict, List, Union, cast, Any, Optional, Literal
# Type ignore for external dependencies without stubs
import spacy  # type: ignore
from spacy.cli import download as spacy_download  # type: ignore
from presidio_analyzer.nlp_engine.spacy_nlp_engine import SpacyNlpEngine  # type: ignore
from presidio_analyzer import AnalyzerEngine, PatternRecognizer  # type: ignore
 
from pii_scanner.regex_patterns.presidio_patterns import patterns
from pii_scanner.check_digit_warehouse.validate_entity_type import validate_entity_check_digit

logger = logging.getLogger(__name__)
 
class LoadedSpacyNlpEngine(SpacyNlpEngine):
    def __init__(self, loaded_spacy_model: Any) -> None:
        super().__init__()
        self.nlp = {"en": loaded_spacy_model}
 
class SpacyNERScanner:
    """
    Optimized NER Scanner using Presidio's AnalyzerEngine with SpaCy.
    """
    SPACY_EN_MODEL = "en_core_web_lg"  # Using smaller model for memory efficiency
 
    def __init__(self) -> None:
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.analyzer: Optional[AnalyzerEngine] = None
        self.nlp_engine = None
        self.initialized = False
        self._nlp_engine_ref: Optional[weakref.ReferenceType] = None  # Weak reference to SpaCy model
        self.region: Optional[str] = None
 
    def __enter__(self) -> 'SpacyNERScanner':
        """Context manager entry"""
        return self
        
    def __exit__(self, exc_type: Optional[type], exc_val: Optional[Exception], exc_tb: Optional[Any]) -> Literal[False]:
        """Context manager exit with cleanup"""
        self.cleanup()
        return False  # Propagate exceptions
        
    def cleanup(self) -> None:
        """Explicit cleanup of resources"""
        if self.analyzer:
            # Clear analyzer references
            if hasattr(self.analyzer, 'nlp_engine'):
                self.analyzer.nlp_engine = None
            self.analyzer = None
            
        # Clear model reference
        self._nlp_engine_ref = None
        # Force garbage collection
        gc.collect()
        self.initialized = False
 
    def _initialize(self) -> None:
        """Lazy initialization of the SpaCy model and Presidio Analyzer."""
        if self.initialized:
            return
 
        try:
            nlp = spacy.load(self.SPACY_EN_MODEL)
        except OSError:
            self.logger.warning("Downloading en_core_web_sm model for SpaCy.")
            spacy_download(self.SPACY_EN_MODEL)
            nlp = spacy.load(self.SPACY_EN_MODEL)
 
        loaded_nlp_engine = LoadedSpacyNlpEngine(loaded_spacy_model=nlp)
        self.analyzer = AnalyzerEngine(nlp_engine=loaded_nlp_engine)
 
        if self.region and hasattr(self.region, 'value'):
            region_value = self.region.value
        else:
            region_value = str(self.region) if self.region else ''
 
        combined_patterns = {**patterns.get("GLOBAL", {}), **patterns.get(region_value, {})}
        recognizers = [PatternRecognizer(supported_entity=entity, patterns=[pattern]) for entity, pattern in combined_patterns.items()]
        
        for recognizer in recognizers:
            self.analyzer.registry.add_recognizer(recognizer)
 
        # Store weak reference to SpaCy model
        self._nlp_engine_ref = weakref.ref(nlp)
        self.initialized = True
 
    async def _process_with_analyzer(self, text: str) -> Dict[str, Union[str, List[Dict[str, str]]]]:
        """Processes text using the Presidio Analyzer."""
        self._initialize()
        if not self.analyzer:
            return {"text": text, "entity_detected": []}
 
        analyzer_results = self.analyzer.analyze(text, language="en")
 
        if not analyzer_results:
            return {"text": text, "entity_detected": []}
 
        entity_type = analyzer_results[0].entity_type
        if self.region and hasattr(self.region, 'value'):
            region_value = self.region.value
        else:
            region_value = str(self.region) if self.region else ''
 
        result = await validate_entity_check_digit(text, entity_type, region_value)
        return cast(Dict[str, Union[str, List[Dict[str, str]]]], result)
 
    async def _process_batch_async(self, texts: List[str]) -> List[Dict[str, Union[str, List[Dict[str, str]]]]]:
        """Processes a batch of texts concurrently using asyncio."""
        results = await asyncio.gather(*(self._process_with_analyzer(text) for text in texts))
        gc.collect()  # Clean up after batch processing
        return results
 
    def _sample_data(self, sample_data: List[str], sample_size: Union[int, float]) -> List[str]:
        """Samples the data based on the given size (integer or percentage)."""
        total = len(sample_data)
        if isinstance(sample_size, float) and 0 < sample_size <= 1:
            size = int(total * sample_size)
        else:
            size = int(sample_size)
        return random.sample(sample_data, min(size, total))
 
    async def scan(self, sample_data: List[str], sample_size: Optional[Union[int, float]], region: str) -> Dict[str, List[Dict[str, Union[str, List[Dict[str, str]]]]]]:
        """Performs an asynchronous scan on the given data."""
        start_time = time.time()
        self.region = region
 
        if sample_size:
            sample_data = self._sample_data(sample_data, sample_size)
 
        results = await self._process_batch_async(sample_data)
 
        self.logger.info(f"Processing completed in {time.time() - start_time:.2f} seconds.")
        gc.collect()  # Final cleanup
        return {"results": results}
 