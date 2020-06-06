'''GUI for the assistant:
running on kivy'''

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class main_window(App):
      
      def build(self):
          return Label(text = "Pulse here to start")


main_window().run()