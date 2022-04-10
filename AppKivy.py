from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.gridlayout import GridyLayout
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (500,550)

class cameraApp(App) :

    def build (self):
        global cameraApp
        cam = Camera()

        btn = Button (text="Capture Image")
        btn.size_hint = (.1,.1)
        btn.font_size = 35
        btn.background_color = 'blue'
        btn.bind (on_press = self.capture_image)
        