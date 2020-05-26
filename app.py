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
      pass


class Speech_To_Text:
      pass


# Initialize the recognizer
rec = sr.Recognizer()

ENG = "en-US"
SPAN = "es-ES"

with sr.Microphone() as source:
     print("Speak to me:\n")

     #adjust the energy threshold based on the surrounding noise level
     rec.adjust_for_ambient_noise(source, duration=0.2)
     audio = rec.listen(source)

     try:
          text = rec.recognize_google(audio, language = ENG)
          print("You told me: {}".format(text))


     except Exception as e:
         print("Sorry, could not understand you, try it again!\n")
     except UnknownValueError:
         print("Error don't known")
