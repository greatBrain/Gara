import speech_recognition as sr
import pyttsx3 as pytt
import os
import re
import webbrowser as wbb

class Text_To_Speech:
  ''' def say_text(command):
          #Initialize the engine
          engine = pytt.init()
          engine.say(command)
          engine.runAndWait() '''


class Speech_To_Text:
      def __init__(self):
          self.ENG = "en-US"
          self.SPAN = "es-ES"

          self.rec = sr.Recognizer()

      def get_speech(self):

           with sr.Microphone() as source:

               print("Speak to me:\n")

               #adjust the energy threshold based on the surrounding noise level
               self.rec.adjust_for_ambient_noise(source, duration=0.2)
               self.audio = self.rec.listen(source)

               try:
                  self.text = self.rec.recognize_google(self.audio, language = self.ENG)
                  print("You told me: {}".format(self.text))

               except Exception as e:
                  print("Sorry, could not understand you, try it again!\n")
               except UnknownValueError:
                  print("Error don't known")

stt = Speech_To_Text()
stt.get_speech()
