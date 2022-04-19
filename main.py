import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image 

import pytesseract

#Database import as well as other necessary imports
import Database
import datetime

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        image=frame;
        image_to_text = pytesseract.image_to_string(image, lang='eng')
        print (image_to_text+"\n____________________________")
        ascii_values = []
        special_characters = "!@#$%^&*()-+?_=,<>/"
        leg="legible"
        nonleg="nonlegible"
        if any(c in special_characters for c in image_to_text):
            bool=leg
        else:
            bool=nonleg
        coordinates = (100,100)
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255,0,0)
        thickness = 2
        image = cv2.putText(image, bool, coordinates, font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.imshow("Text", image)
   
# Displaying the image
cv2.imshow(window_name, image)



#I am assuming image_to_text is the serial
#Inserting Data into database
#Example: insertDATA("19:51/4/14/22", "S158392", "C:\Users\Blood\source\repos\CSE-120-324-Project\IMG.png")
img_name = datetime.datetime
img_name_jpg = img_name+".jpg"
cv2.imwrite(img_name, image)
insertDATA(datetime.datetime, image_to_text, img_name_jpg)

cam.release()

cv2.destroyAllWindows()