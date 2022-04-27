from imutils import paths
import argparse
import sys
import numpy as np
import cv2
from PIL import ImageFont, ImageDraw, Image 



#Database import as well as other necessary imports
import Database
import datetime



cam = cv2.VideoCapture(0)



img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.namedWindow("SpringScan", cv2.WINDOW_NORMAL)
    cv2.moveWindow("SpringScan", 100,100);
 
    cv2.imshow("SpringScan", frame)
    

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        image=frame;
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = cv2.Laplacian(image, cv2.CV_64F).var()
        print(fm)
        leg = cv2.imread('leg.png')
        nonleg = cv2.imread('nonleg.png')
        if fm <90:
            result=nonleg
        else:
            result=leg

        position = (10,50)
        cv2.putText(
            image, #numpy array on which text is written
            "CAPTURED SPRING:", #text
            position, #position at which writing has to start
            cv2.FONT_HERSHEY_SIMPLEX, #font family
            1, #font size
            (0,204,0), #font color
            3) #font stroke

        cv2.imshow('CAPTURED SPRING', image)
        cv2.imshow('Result', result)

   
# Displaying the image



#I am assuming image_to_text is the serial
#Inserting Data into database
#Example: insertDATA("19:51/4/14/22", "S158392", "C:\Users\Blood\source\repos\CSE-120-324-Project\IMG.png")
#img_name = datetime.datetime
#img_name_jpg = img_name+".jpg"
#cv2.imwrite(img_name, image)
#insertDATA(datetime.datetime, image_to_text, img_name_jpg)

cam.release()
cv2.destroyAllWindows()
