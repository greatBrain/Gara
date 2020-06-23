from playsound import playsound
import date_time_handler as dth

class Audio:
    def __init__(self):
        self.date_time_handler = dth.Date_And_Time()

    def play_audio(self, audio_file):
        self.audio_file = audio_file
        playsound(self.audio_file)

    def greet(self):

        self.time = list(self.date_time_handler.get_time())
        self.entire_time = ''.join(self.time)
        self.hour = int(self.entire_time[0:2])


        if self.hour >= 1 and self.hour <= 12:
           self.play_audio('audio/welcome_day.wav')

        elif self.hour >= 13 and self.hour <= 19:
             self.play_audio('audio/welcome_noon.wav')

        elif self.hour >= 20 and self.hour <= 23:
             self.play_audio('audio/welcome_night.wav')
