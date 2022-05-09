from imutils import paths
import argparse
import sys
import numpy as np
import cv2
import os
import mysql.connector
from PIL import ImageFont, ImageDraw, Image 




#Database import as well as other necessary imports
from Database import insertDATA, convertFileToName
import datetime

i=0


#starting camera
cam = cv2.VideoCapture(0)



i = 0

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
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        image=frame;
        #calculating legibility threshold
        thresh = cv2.Laplacian(image, cv2.CV_64F).var()
        leg = cv2.imread('leg.png')
        nonleg = cv2.imread('nonleg.png')
        
        
        #determining if image is legible based on threshold
        if thresh <90:
            fontcolor=(0,0,255)
            result=nonleg
        else:
            fontcolor=(0,204,0)
            result=leg
           
        #outputting captured spring   
        position = (10,50)
        cv2.putText(
            image, 
            "CAPTURED SPRING:", 
            position, 
            cv2.FONT_HERSHEY_SIMPLEX, 
            1, 
            fontcolor, 
            3) 
        #Test var example
        path = 'springs'
        #writing the image to a file
        img_name = "spring{}.png".format(i+1)
        cv2.imwrite(os.path.join(path , img_name), frame)
        cv2.waitKey(0)
        i += 1
       
        

        cv2.imshow('CAPTURED SPRING', image)
        #showing legibility
        cv2.imshow('Result', result)

       

   






cam.release()
cv2.destroyAllWindows()
