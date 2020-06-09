'''GUI for the assistant:
running on kivy'''

import src
import main
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from screeninfo import get_monitors
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

       '''def build(self):
          Config.set('graphics', 'resizable', False)          
          #Window.clearcolor = (1, 1, 1, 1)
          Window.size = (540,600)
          return self'''

       def build(self):
            # create a fully styled functional button 
            # Adding images normal.png and down.png 

            Config.set('graphics', 'resizable', False)          
            Window.clearcolor = (1, 1, 1, 1)
            Window.size = (550,580)            
            Window.set_system_cursor("hand")
            
            self.btn = Button(background_normal = 'src/mic.png',
                  size_hint = (.8, .8), 
                  pos_hint = {"x":0.10, "y":0.2} 
            )

            # bind() use to bind the button to function callback  
            self.btn.bind(on_press = self.callback)  
            return self.btn  
    
       # callback function tells when button pressed  
       def callback(self, event):
         self.main = main.Speech()
         self.main.get_speech()
         self.main.run_command()


if __name__ == "__main__":
     #Write the configuration made into a file:
     Config.write()    
     main_window().run()
     