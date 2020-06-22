from playsound import playsound
import time

class Audio:
    def __init__(self, ):
        pass

    def play_audio(self, audio_file):
        self.audio_file = audio_file
        playsound(self.audio_file)

    def greet(self):
        """Get the current time and convert the string representing hour in a int"""

        self.time = time.localtime(time.time())
        self.current_time = time.strftime("%H:%M:%S", self.time)
        list(self.current_time)
        self.hour = int(self.current_time[0:2])

        if self.hour >= 1 and self.hour <= 12:
           self.play_audio('audio/welcome_day.wav')

        elif self.hour >= 13 and self.hour <= 19:
             self.play_audio('audio/welcome_noon.wav')

        elif self.hour >= 20 and self.hour <= 23:
             self.play_audio('audio/welcome_night.wav')
