import speech_recognition as sr
import pyttsx3 as pytt
import os
import subprocess as subp
import re
from time import *
import webbrowser as wbb
import requests as rqs

class Text_To_Speech:
  ''' def say_text(command):
          #Initialize the engine
          engine = pytt.init()
          engine.say(command)
          engine.runAndWait() '''


class Speech:
      def __init__(self):
          self.ENG = "en-US"
          self.ESP = "es-ES"

          #self.protocols = ["http://www.", "http://www.", "ftp."]
          self.HTTP = "http://www."
          self.HTTPS = "http://www."

          self.domains = ['.com', '.net', 
                          '.org', '.es', 
                          '.co', '.do'
                         ]

          self.commands = {'open':'abre', 
                           'close':'cierra',
                           'tell':'dime', 
                           'check':'revisa',
                           'turn on':'enciende',
                           'shutdown':'apaga',
                           'search for':'busca',
                           'what is the time':'que hora es'
                         } 


          self.rec = sr.Recognizer()

      def get_speech(self):

           with sr.Microphone() as source:
               print("Speak to me:\n")

               #adjust the energy threshold based on the surrounding noise level
               self.rec.adjust_for_ambient_noise(source, duration=0.2)
               self.audio = self.rec.listen(source)

               try:
                  self.text = self.rec.recognize_google(self.audio, language = self.ESP).lower()
                  self.text = str(self.text)
                  print("You told me: {}".format(self.text))
               except Exception as e:
                  print("Sorry, could not understand you, try it again!\n")
               except UnknownValueError:
                  print("Error don't known")

      def run_command(self): 
            
            try: 
               #Split the text said by user to obatin a command and the web/app to work in 
               self.text_splited = re.split(' ',self.text)

               self.app = ''            
               self.web_page = ''

               for eng, esp in self.commands.items():
                   if re.search(eng, self.text_splited[0]) or re.search(esp, self.text_splited[0]):
                      if re.search(self.text_splited[1], self.text):
                         #subp.call('atom') 
                         
                         try:
                            pass
                         except Exception as e:
                            raise e
                         finally:
                            pass
                   else:
                      print("Sorry, something is wrong.. Try it again!\n")


               
               '''if re.search("open", self.text):
                  self.command = (self.HTTPS + self.page_name + self.domains[0])
                  wbb.open(self.command)'''

            except Exception as e:
                   raise e


      def add_to_file(self, word):
          self.words = open("words.txt", "w+")

          for i in len(words):
             self.words.write(i)

          self.words.close()

sp = Speech()
sp.get_speech()
sp.run_command()
