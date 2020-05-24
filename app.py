import speech_recognition as sr
import pyttsx3 as pytt
import os
import re
import webbrowser as wbb


# Initialize the recognizer  
rec = sr.Recognizer() 

def say_text(command):    

    #Initialize the engine
    engine = pytt.init()

    engine.say(text)    
    engine.runAndWait() 

while(True):
    # Exception handling to handle 
    try:

      # use the microphone as source for input.
      with sr.Microphone() as source2:
          # wait for a second to let the recognizer 
          # adjust the energy threshold based on 
          # the surrounding noise level
          rec.adjust_for_ambient_noise(source2, duration=0.2)


          #listens for the user's input 
          audio2 = rec.listen(source2)

          # Using ggogle to recognize audio
          user_text = rec.recognize_google(audio2)
          user_text = user_text.lower()

          print("You said" + " " + user_text)

          say_text(user_text)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Unknown error has occured!")     
