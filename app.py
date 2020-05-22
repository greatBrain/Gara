import speech_recognition as sr
import pyttsx3 as pytt
import os
import re
import webbrowser as wbb

def create_engine(command):
    text = str(command)
    engine = pytt.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.say(text)    
    engine.runAndWait()

    
create_engine(input("write your command:"))



'''Cahange the voice(optional)
    change_voice = input("Do you want to change the voice y/n?\n")

    if 'y' in change_voice:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

        engine.say("i hope you like my new voice") 
    else:
        pass'''