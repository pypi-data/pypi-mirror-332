

import cv2, pytesseract, difflib
from pii_scanner.octopii import image_utils, file_utils, text_utils

import os

from skimage.transform import rotate
from deskew import determine_skew
import numpy


def scan_image_for_people(image):
    # Convert the image to a numpy array
    image = numpy.array(image)
    
    # Adjusted file path for the cascade file
    cascade_file_path = os.path.join(os.path.dirname(__file__), 'files_store', 'face_cascade.xml')
    
    # Check if the cascade file exists
    if not os.path.exists(cascade_file_path):
        raise FileNotFoundError(f"The file '{cascade_file_path}' was not found. Please ensure the file exists in the correct directory.")
    
    # Load the cascade classifier
    cascade_classifier = cv2.CascadeClassifier(cascade_file_path)
    
    # Check if the classifier loaded correctly
    if cascade_classifier.empty():
        raise ValueError(f"Failed to load cascade classifier from '{cascade_file_path}'. The file might be corrupt or incompatible.")
    
    # Detect faces in the image
    faces = cascade_classifier.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    return len(faces)


def scan_image_for_text(image):
    image = numpy.array(image) # converts the image to a compatible format

    # 0. Original 
    #print ("Reading text from unmodified image")
    try:
        image_text_unmodified = pytesseract.image_to_string(image, config = '--psm 12')
    except TypeError:
        print("Cannot open this file type.")
        return
    #cv2.imwrite("image0.png", image)

    # 1. Auto-rotation
    try: 
        #print ("Attempting to auto-rotate image and read text")
        try:
            degrees_to_rotate = pytesseract.image_to_osd(image)
        except: degrees_to_rotate = "Rotate: 180"

        for item in degrees_to_rotate.split("\n"):
            if "rotate".lower() in item.lower():
                degrees_to_rotate = int(item.replace(" ", "").split(":", 1)[1])
                if degrees_to_rotate == 180:
                    pass
                elif degrees_to_rotate == 270:
                    image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
                elif degrees_to_rotate == 360:
                    image = cv2.rotate(image, cv2.ROTATE_180)

        image_text_auto_rotate = pytesseract.image_to_string(image, config = '--psm 12')
        #cv2.imwrite("image1.png", image)
    except: 
        print ("Couldn't auto-rotate image")
        image_text_auto_rotate = ""

    # 2. Grayscaled
    try: 
        #print ("Reading text from grayscaled image")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_text_grayscaled = pytesseract.image_to_string(image, config = '--psm 12')
        #cv2.imwrite("image2.png", image)
    except: 
        print ("Couldn't grayscale image")
        image_text_grayscaled = ""

    # 3. Monochromed
    try: 
        #print ("Reading text from monochromed image")
        image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        image_text_monochromed = pytesseract.image_to_string(image, config = '--psm 12')
        #cv2.imwrite("image3.png", image)
    except: 
        print ("Couldn't monochrome image")
        image_text_monochromed = ""

    # 4. Mean threshold
    try:
        #print ("Reading text from mean threshold image")
        image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        image_text_mean_threshold = pytesseract.image_to_string(image, config = '--psm 12')
        #cv2.imwrite("image4.png", image)
    except: 
        print ("Couldn't mean threshold image")
        image_text_mean_threshold = ""

    # 5. Gaussian threshold
    try:
        #print ("Reading text from gaussian threshold image")
        image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)
        image_text_gaussian_threshold = pytesseract.image_to_string(image, config = '--psm 12')
        #cv2.imwrite("image5.png", image)
    except: 
        print ("Couldn't gaussian threshold image")
        image_text_gaussian_threshold = ""

    # 6. Deskew
    try:
        # 6a. Deskew one
        #print ("First attempt at de-skewing image and reading text")
        angle = determine_skew(image)
        rotated = rotate(image, angle, resize=True) * 255
        image = rotated.astype(numpy.uint8)
        image_text_deskewed_1 = pytesseract.image_to_string(image, config = '--psm 12')
        #cv2.imwrite("image6.png", image)

        # 6b. Deskew two
        #print ("Second attempt at de-skewing image and reading text")
        angle = determine_skew(image)
        rotated = rotate(image, angle, resize=True) * 255
        image = rotated.astype(numpy.uint8)
        image_text_deskewed_2 = pytesseract.image_to_string(image, config = '--psm 12')
        #cv2.imwrite("image7.png", image)

        # 6c. Deskew three
        #print ("Third attempt at de-skewing image and reading text")
        angle = determine_skew(image)
        rotated = rotate(image, angle, resize=True) * 255
        image = rotated.astype(numpy.uint8)
        image_text_deskewed_3 = pytesseract.image_to_string(image, config = '--psm 12')
        #cv2.imwrite("image8.png", image)
    except: 
        print ("Couldn't deskew image")
        image_text_deskewed_1 = ""
        image_text_deskewed_2 = ""
        image_text_deskewed_3 = ""

    # END OF IMAGE PROCESSING AND OCR

    # Tokenize all scanned strings by newlines and spaces
    unmodified_words = text_utils.string_tokenizer(image_text_unmodified)
    grayscaled = text_utils.string_tokenizer(image_text_grayscaled)
    auto_rotate = text_utils.string_tokenizer(image_text_auto_rotate)
    monochromed = text_utils.string_tokenizer(image_text_monochromed)
    mean_threshold = text_utils.string_tokenizer(image_text_mean_threshold)
    gaussian_threshold = text_utils.string_tokenizer(image_text_gaussian_threshold)
    deskewed_1 = text_utils.string_tokenizer(image_text_deskewed_1)
    deskewed_2 = text_utils.string_tokenizer(image_text_deskewed_2)
    deskewed_3 = text_utils.string_tokenizer(image_text_deskewed_3)

    original = image_text_unmodified + "\n" + image_text_auto_rotate + "\n" + image_text_grayscaled + "\n" + image_text_monochromed + "\n" + image_text_mean_threshold + "\n" + image_text_gaussian_threshold + "\n" + image_text_deskewed_1 + "\n" + image_text_deskewed_2 + "\n" +  image_text_deskewed_3

    intelligible = unmodified_words + grayscaled + auto_rotate + monochromed + mean_threshold + gaussian_threshold + deskewed_1 + deskewed_2 + deskewed_3

    return (original, intelligible)
