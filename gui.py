'''GUI for the assistant:
running on kivy'''

import src
import main
from audio import *
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
#from screeninfo import get_monitors
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.config import Config

'''Builder.load_string("""

<main_window>:

    source: 'src/mic.png'
    
    
    on_release:
       
       
        self.text = "hola"
    
""") '''

class main_window(Button, ButtonBehavior, Image, App, BoxLayout):

       def play_welcome_audio(self):
           audio = main.audio('audio/welcome_night.wav')
           audio.play_audio()


       def build(self):
            self.play_welcome_audio()
            Config.set('graphics', 'resizable', False)
            Window.clearcolor = (0,0,0,0)
            Window.size = (490,600)            
            Window.set_system_cursor("hand")

            self.btn = Button(background_normal = 'src/mic.png',
                  size = (100, 25),               
                  size_hint = (.8, .7), 
                  pos_hint = {"x":0.12, "y":0.2} 
            )

            # bind() use to bind the button to function callback  
            self.btn.bind(on_press = self.callback)  
            return self.btn  
    
       # callback function, when button pressed, 
       # create a main object and then calls its two funtions:  
       def callback(self, event):
         self.main = main.Speech()
         self.main.get_speech()
         self.main.run_command()


if __name__ == "__main__":
     #Write the configuration made into a file:
     Config.write()    
     main_window().run()
     
