from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = Image.open('test2.png')

image_to_text = pytesseract.image_to_string(image, lang='eng')

print (image_to_text+"hi")

#def test(self):
        #image = Image.open('IMG.PNG')
        #print(pytesseract.image_to_string(image, lang='eng'))

