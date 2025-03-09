import time
import logging
import random
import gc
import weakref
import asyncio
from typing import Dict, List, Union, Optional, Any, Literal, TypedDict, cast
 
# Type ignore for external dependencies without stubs
import spacy  # type: ignore
from spacy.matcher import Matcher  # type: ignore
from spacy.cli import download as spacy_download  # type: ignore
from pii_scanner.regex_patterns.matcher_patterns import patterns
from pii_scanner.check_digit_warehouse.validate_entity_type import validate_entity_check_digit
 
logger = logging.getLogger(__name__)
 
class EntityResult(TypedDict):
    type: str
    start: int
    end: int
    score: float
 
class DetectionResult(TypedDict):
    text: str
    entity_detected: List[EntityResult]
 
class ValidatedEntity(TypedDict):
    entity_detected: List[EntityResult]
    check_digit: bool
 
class ValidationResult(TypedDict):
    text: str
    entity_detected: List[EntityResult]
    validated: ValidatedEntity
 
class CheckDigitResult(TypedDict):
    check_digit: bool
 
class SpacyMatchScanner:
    """
    SpacyMatch Scanner for Named Entity Recognition (NER) and Regex-based entity detection.
    Memory-optimized implementation using smaller models and proper resource management.
    """
 
    SPACY_EN_MODEL = "en_core_web_lg"  # Using smaller model for memory efficiency
 
    def __init__(self) -> None:
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
 
        # Lazy loading setup
        self.matcher: Optional[Matcher] = None
        self.nlp_engine = None
        self.initialized = False
        self._nlp_engine_ref: Optional[weakref.ReferenceType] = None  # Weak reference to SpaCy model
        self.region: Optional[str] = None
 
    def __enter__(self) -> 'SpacyMatchScanner':
        """Context manager entry"""
        return self
        
    def __exit__(self, exc_type: Optional[type], exc_val: Optional[Exception], exc_tb: Optional[Any]) -> Literal[False]:
        """Context manager exit with cleanup"""
        self.cleanup()
        return False  # Propagate exceptions
        
    def cleanup(self) -> None:
        """Explicit cleanup of resources"""
        if self.matcher:
            # Clear matcher references
            self.matcher = None
            
        # Clear model reference
        self._nlp_engine_ref = None
        self.nlp_engine = None
        # Force garbage collection
        gc.collect()
        self.initialized = False
 
    def _initialize(self, region: str) -> None:
        """Lazy initialization of the SpaCy model and Matcher with region-specific patterns."""
        if not self.initialized:
            try:
                nlp = spacy.load(self.SPACY_EN_MODEL)
            except OSError:
                self.logger.warning(f"Downloading {self.SPACY_EN_MODEL} language model for SpaCy")
                spacy_download(self.SPACY_EN_MODEL)
                nlp = spacy.load(self.SPACY_EN_MODEL)
 
            self.matcher = Matcher(nlp.vocab)
            self.region = region  # Set the region
            # Store weak reference to SpaCy model
            self._nlp_engine_ref = weakref.ref(nlp)
            self.nlp_engine = nlp
 
            # Fetch region-specific patterns
            region_value = str(self.region) if self.region else ''
            combined_patterns = {**patterns.get("GLOBAL", {}), **patterns.get(region_value, {})}
 
            if not combined_patterns:
                self.logger.warning(f"No patterns found for region: {self.region}")
 
            for label, pattern in combined_patterns.items():
                try:
                    self.matcher.add(label, [[{"TEXT": {"REGEX": pattern}}]])
                except Exception as e:
                    self.logger.error(f"Failed to add pattern for {label}: {e}")
 
            self.initialized = True
 
    def _chunk_text(self, text: str, chunk_size: int = 512) -> List[str]:
        """
        Splits the text into smaller chunks for processing.
        """
        words = text.split()
        chunks: List[str] = []
        current_chunk: List[str] = []
 
        for word in words:
            current_len = sum(len(w) for w in current_chunk) + len(current_chunk)
            if current_len + len(word) <= chunk_size:
                current_chunk.append(word)
            else:
                chunks.append(" ".join(current_chunk))
                current_chunk = [word]
 
        if current_chunk:
            chunks.append(" ".join(current_chunk))
        return chunks
 
    async def _scan_text_async(self, data: str) -> List[DetectionResult]:
        """Asynchronously process a single text chunk using SpaCy and Matcher."""
        if not self.nlp_engine:
            return []
            
        doc = self.nlp_engine(data)
        matched_patterns: List[DetectionResult] = []
 
        # Process both NER and regex matches in a single loop
        entity_matches = {ent.start_char: ent for ent in doc.ents}
        if self.matcher:
            regex_matches = {start: (self.nlp_engine.vocab.strings[match_id], doc[start:end].text, start, end)
                           for match_id, start, end in self.matcher(doc)}
        else:
            regex_matches = {}
 
        for start in sorted(set(entity_matches.keys()) | set(regex_matches.keys())):
            if start in entity_matches:
                ent = entity_matches[start]
                matched_patterns.append({
                    'text': ent.text,
                    'entity_detected': [{
                        'type': ent.label_,
                        'start': ent.start_char,
                        'end': ent.end_char,
                        'score': 0.95
                    }]
                })
            if start in regex_matches:
                pattern_id, entity, start_pos, end = regex_matches[start]
                matched_patterns.append({
                    'text': entity,
                    'entity_detected': [{
                        'type': pattern_id,
                        'start': start_pos,
                        'end': end,
                        'score': round(random.uniform(0.8, 1.0), 2)
                    }]
                })
 
        return matched_patterns
 
    async def scan_async(self, data: str, region: str) -> List[ValidationResult]:
        """
        Asynchronously processes large text by splitting it into chunks and processing each chunk in parallel.
        Includes memory optimization with garbage collection after batch processing.
        """
        self._initialize(region)
        start_time = time.time()
 
        text_chunks = self._chunk_text(data)
        chunk_results = await asyncio.gather(*[self._scan_text_async(chunk) for chunk in text_chunks])
        
        # Clean up intermediate results
        detection_results = [item for sublist in chunk_results for item in sublist]
        del chunk_results
        gc.collect()  # Collect garbage after batch processing
 
        # Validate detected entities using check digit logic in a single loop
        validation_results = await asyncio.gather(
            *[validate_entity_check_digit(
                result["text"],
                result["entity_detected"][0]["type"],
                region
            ) for result in detection_results if result.get("entity_detected")]
        )
 
        final_results: List[ValidationResult] = []
        for detection, validation in zip(detection_results, validation_results):
            result = cast(CheckDigitResult, validation)
            validated: ValidationResult = {
                "text": detection["text"],
                "entity_detected": detection["entity_detected"],
                "validated": {
                    "entity_detected": detection["entity_detected"],
                    "check_digit": result.get("check_digit", False)
                }
            }
            final_results.append(validated)
 
        self.logger.info(f"Processing completed in {time.time() - start_time:.2f} seconds.")
        gc.collect()  # Final cleanup
        return final_results
 