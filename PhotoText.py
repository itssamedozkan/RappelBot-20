# import the necessary packages
from PIL import Image
import pytesseract
import cv2
import os
def GetText(image):
    proces = "thresh"
    # load the example image and convert it to grayscale

    

    gray = cv2.resize(image, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    invert = cv2.bitwise_not(gray)

    if proces == "thresh":
        gray = cv2.threshold(invert, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # make a check to see if median blurring should be done to remove
    # noise
    elif proces == "blur":
        gray = cv2.medianBlur(invert, 3)

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, invert)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    return str(text)


