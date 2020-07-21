from playsound import playsound
import date_time_handler as dth
import text_to_speech as ttsp

class Audio:
    def __init__(self):
        self.date_time_handler = dth.Date_And_Time()
        self.hour = int()

    def play_audio(self, audio_file):
        playsound(audio_file)
