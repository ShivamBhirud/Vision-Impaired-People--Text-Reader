# from PIL import Image
import pytesseract
import cv2 as cv
import os
import pyttsx3

# load the example image and convert it to grayscale
image = cv.imread("/home/shivam/Project_VisionImpared_helper/example_04.png")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# out=cv.transpose(gray)
# gray=cv.flip(out,flipCode=0)

gray = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
# gray = cv.medianBlur(gray, 3)


# load the image, apply OCR using pytesseract
text = pytesseract.image_to_string(gray)
print(text)

# convert text to audio
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 40)
engine.say(text)
engine.runAndWait()
 
# show the output images
cv.imshow("Image", image)
cv.imshow("Output", gray)
cv.waitKey(0)
