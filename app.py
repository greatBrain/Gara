import speech_recognition as sr
import pyttsx3 as pytt
import os
import subprocess as subp
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
                           'search for':'busca'
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
                  print("You told me: {}".format(self.text))
               except Exception as e:
                  print("Sorry, could not understand you, try it again!\n")
               except UnknownValueError:
                  print("Error don't known")

      def run_command(self): 
            
            try:  
               self.app = ''            
               self.web_page = ''

               #if re.match("akira", self.text):
               for eng, esp in self.commands.items():
                   if re.search(eng, self.text) or re.search(esp, self.text):
                      if re.search("atom", self.text):
                         subp.call('atom')  


               
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
