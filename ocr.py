import cv2
import pytesseract

im=cv2.imread('Righ.png')
config=('-l eng --oem 1 --psm 3')
text= pytesseract.image_to_string(im,config=config)

print(text)