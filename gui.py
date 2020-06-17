'''GUI for the assistant:
running on kivy'''

import src
import main
from audio import *
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
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
           """Get the current time and convert the string representing hour in a int"""

           self.time = time.localtime(time.time())
           self.current_time = time.strftime("%H:%M:%S", self.time)

           list(self.current_time)
           self.hour = int(self.current_time[0:2])

           if self.hour >=1 and self.hour<= 12:
               self.audio_class = main.Audio('audio/welcome_day.wav')
               self.audio_class.play_audio()
               del(audio)
           elif self.hour >=13 and self.hour<=19:
               self.audio_class = main.Audio('audio/welcome_noon.wav')
               self.audio_class.play_audio()
               del(self.audio_class)
           elif self.hour >= 20 and self.hour<= 23:
               self.audio_class = main.Audio('audio/welcome_night.wav')
               self.audio_class.play_audio()
               del(self.audio_class)

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
     
