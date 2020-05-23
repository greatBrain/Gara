import speech_recognition as sr
import pyttsx3 as pytt
import os
import re
import webbrowser as wbb


'''class Assistant: 
ass = Assistant()    
ass.say_text(input("write your command:")) '''        

def say_text(self, text):

    # Initialize the recognizer  
    rec = sr.Recognizer()  

    self.text = str(text)
    self.engine = pytt.init()

    self.engine.say(text)    
    self.engine.runAndWait() 

    while(True):
        # Exception handling to handle 
        try:

           # use the microphone as source for input.
           with sr.Microphone() as source2:
               # wait for a second to let the recognizer 
               # adjust the energy threshold based on 
               # the surrounding noise level
               rec.adjust_for_ambient_noise(source2, duration=0.2)


        except expression as identifier:
            pass
        
          
          
















