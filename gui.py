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

'''Builder.load_string("""

<main_window>:

    source: 'src/mic.png'
    
""") '''


class main_window(ButtonBehavior, Image, App, BoxLayout):     

      def build(self):
          Config.set('graphics', 'resizable', False)          
          Window.clearcolor = (1, 1, 1, 1)
          Window.size = (540,600)
          return self

if __name__ == "__main__":
     #Write the configuration made into a file:
     Config.write()    
     main_window().run()
     