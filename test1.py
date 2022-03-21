from unittest import result
from pytesseract import Output 
import pytesseract
import cv2

image = cv2.imread("images_0.jpg")
x = 0
y = 0
w = 1080
h = 800
image = image[y: y+h,x: x+w]
rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

results = pytesseract.image_to_data(rgb,output_type=Output.DICT,lang='chi_tra',config='--psm 11')

print(results['text'])