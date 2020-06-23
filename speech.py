import speech_recognition as sr
#import pyttsx3 as pytt
import audio_handler

class Speech:
    def __init__(self):
        self.audio = audio_handler.Audio()
        self.audio.greet()
        self.rec = sr.Recognizer()

        # Supported laanguages
        self.ENG = "en-US"
        self.ESP = "es-ES"

    def get_speech(self):

        with sr.Microphone() as source:
             print("Speak to me:\n")

             # adjust the energy threshold based on the surrounding noise level
             self.rec.adjust_for_ambient_noise(source, duration=0.2)
             self.audio = self.rec.listen(source)

             try:
                 self.text = self.rec.recognize_google(self.audio, language=self.ESP).lower()
                 self.text = str(self.text)
                 print("You told me: {}".format(self.text))

             except Exception as e:
                 print("Sorry, could not understand you, try it again!\n")

             except sr.UnknownValueError:
                 print("Error don't known")

    def get_command(self):
        return self.text
