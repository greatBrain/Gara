import speech_recognition as sr
import pyttsx3 as pytt
import os
import subprocess as subp
import re
from time import *
import webbrowser as wbb
import requests 
from requests.exceptions import MissingSchema

class Text_To_Speech:
  ''' def say_text(command):
          #Initialize the engine
          engine = pytt.init()
          engine.say(command)
          engine.runAndWait() '''


class Speech:
      def __init__(self):

          #Supported laanguages
          self.ENG = "en-US"
          self.ESP = "es-ES"

          #self.protocols = ["http://www.", "http://www.", "ftp."]
          self.HTTP = "http://www."
          self.HTTPS = "http://www."

          self.domains = ['.com', '.org', 
                          '.net', '.es'
                         ]

          self.commands = {'open':'abre',
                           'openweb': 'abrelapagina',
                           'openprogram': 'abrelaaplicacion',
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
               #self.command = self.text_splited[0] + self.text_splited[1]

               for eng, esp in self.commands.items():
                   for i in range(len(self.text_splited)):
                       if re.search(eng,self.text_splited[i]) or re.search(esp,self.text_splited[i]): 
                          #Call open_web, or open_app function
                          #self.open_app(self.text_splited[i+1])
                          self.open_web(self.text_splited[i+1])
                          #pass                     
                       else:
                          print("Sorry, something is wrong.. Try it again!\n")

            except Exception as e:
                   print("Command invalid. Please check the availeable commands that you can tell me!\n")
                   raise e

      def open_web(self, web_name):
           
           try:              
              self.stop = True

              while self.stop:                  
                  for dom in range(len(self.domains)):
                      self.website = (self.HTTPS + web_name + self.domains[dom])                     
                      self.request = requests.get(self.website)

                      if self.request:
                         wbb.open(self.website)
                         self.stop = False                      
                      else:
                         continue              

           except MissingSchema as m:
              print("The provided URL is invalid. Try again!\n")
              raise m
           except Exception as e:
              raise e
           finally:
              pass
      
      def open_app(self, app):
          subp.call(app)

      def add_to_file(self, word):
          self.words = open("words.txt", "w+")

          for i in len(words):
             self.words.write(i)
          self.words.close()

sp = Speech()
sp.get_speech()
sp.run_command()
