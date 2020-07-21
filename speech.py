import speech_recognition as sr
from text_to_speech import Text_To_Speech

class Speech:
    def __init__(self):
        self.rec = sr.Recognizer()        

        # Supported laanguages
        self.ENG = "en-US"
        self.ESP = "es-ES"

    def get_speech(self):
        with sr.Microphone() as source:
             print("Speak to me:\n")

             # adjust the energy threshold
             self.rec.adjust_for_ambient_noise(source, duration=2)
             self.audio = self.rec.listen(source)

             try:
                 self.voice = self.rec.recognize_google(self.audio, language=self.ENG).lower()
                 return self.voice

             except Exception as e:
                 Text_To_Speech().translate_and_play("Sorry, could not understand you, try it again!\n")

             except sr.UnknownValueError:
                 print("Error don't known")