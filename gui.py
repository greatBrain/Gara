'''GUI for the assistant:
running on kivy'''

import src
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


Config.set('graphics', 'resizable', False)
Window.clearcolor = (1, 1, 1, 1)

Builder.load_string("""

<main_window>:

    source: 'src/mic.png'
    
""")


class main_window(ButtonBehavior, Image, App, BoxLayout):
              
      '''def build(self):
         self.btn = Button(
                     background_normal = 'src/mic.png', 
                     #background_down = 'down.png', 
  
                     # Added the border property to round the corners of the button 
                     border = (30, 30, 30, 30),
                       
                     size_hint = (.3, .3), 
                     pos_hint = {"x":0.35, "y":0.3} 
                   )  
  
        # Returning the button 
         return self.btn '''

      def build(self):
          return self

if __name__ == "__main__":    
     main_window().run()