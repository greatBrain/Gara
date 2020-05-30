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


class Speech:
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
                  self.text = self.rec.recognize_google(self.audio, language = self.ENG).lower()
                  print("You told me: {}".format(self.text))
               except Exception as e:
                  print("Sorry, could not understand you, try it again!\n")
               except UnknownValueError:
                  print("Error don't known")

      def run_command(self):
           self.HTTP = "http://www."
           self.HTTPS = "https://www."
           self.domains = ['.com', '.net', '.org']
           self.page_name = ''

           if re.search("abrir", self.text):
               if re.search("facebook", self.text):
                  try:
                     self.page_name = "facebook"
                     self.command = (self.HTTPS + self.page_name + self.domains[0])
                     wbb.open(self.command)
                  except Exception as e:
                     raise e

     def add_to_file(self, word):
         self.word = open("words.txt", "w+")

         for i in len(word):
             self.word.write(i)

         self.word.close()

sp = Speech()
sp.get_speech()
sp.run_command()
