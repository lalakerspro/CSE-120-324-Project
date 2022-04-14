'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)
import numpy
from PIL import Image
from kivy.uix.camera import Camera



from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

import time

#from android.permissions import request_permissions, Permission
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (1920, 1080)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: 
            root.capture()
            root.printInfo()
            
''')


class CameraClick(BoxLayout):
   
    def capture(self):
        
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG.png")
        print("Captured")
       
        

      
     
    
    def printInfo(self):
        image = Image.open("IMG.png")
        leg=image_to_text = pytesseract.image_to_string(image, lang='eng')
   
        print(str(leg))
        print("____________________")
        return leg;

      

class TestCamera(App):

    def build(self):
        #request_permissions([Permission.CAMERA,
                            #Permission.WRITE_EXTERNAL_STORAGE,
                            #Permission.READ_EXTERNAL_STORAGE])

        return CameraClick()


TestCamera().run()
