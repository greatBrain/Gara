""" Module to translate text to speech """
from gtts import gTTS
import audio_handler

class Text_To_Speech:
      def __init__(self):
          self.audio_handler_obj = audio_handler.Audio()

      def translate_and_play(self, text):
          try:
              self.gtss_obj = gTTS(text=text, lang='es', slow=False)

              # Save the audio generated.
              self.gtss_obj.save('audio/task_reminder.mp3')

              # Play the audio in the audio handler module:
              self.audio_handler_obj.play_audio('audio/task_reminder.mp3')

          except Exception as e:
              print("Error translating to voice\n")
              print(e)

