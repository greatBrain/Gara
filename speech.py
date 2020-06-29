import speech_recognition as sr

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
             self.rec.adjust_for_ambient_noise(source, duration=3)
             self.audio = self.rec.listen(source)

             try:
                 self.voice = self.rec.recognize_google(self.audio, language=self.ENG).lower()
                 return self.voice

             except Exception as e:
                 print("Sorry, could not understand you, try it again!\n")

             except sr.UnknownValueError:
                 print("Error don't known")