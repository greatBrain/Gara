from playsound import playsound
import date_time_handler as dth
import text_to_speech as ttsp

class Audio:
    def __init__(self):
        self.date_time_handler = dth.Date_And_Time()
        self.hour = int()

    def play_audio(self, audio_file):
        playsound(audio_file)


    def set_hour_to_int(self):
        self.time = list(self.date_time_handler.get_time())
        self.entire_time = ''.join(self.time)

        self.hour = int(self.entire_time[0:2])

    def set_greettings(self):
        self.greettings = [
            "good morning how can i help you?",
            "good afternoon how can i help you?",
            "good night, how can i help you?"
        ]
        return self.greettings

    def greet(self):
        if self.hour >= 1 and self.hour <= 12:
           self.play_audio('audio/welcome_day.wav')

        elif self.hour >= 13 and self.hour <= 19:
             self.play_audio('audio/welcome_noon.wav')

        elif self.hour >= 20 and self.hour <= 23:
             self.play_audio('audio/welcome_night.wav')