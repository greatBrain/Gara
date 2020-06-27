""" Module to translate text to speech """
from gtts import gTTS
import audio_handler

class Text_To_Speech:
      def __init__(self, text):
          self.text = text
          self.audio_handler_obj = audio_handler.Audio()

      def translate(self):
          self.gtss_obj = gTTS(text=self.text, lang='en', slow=False)

      def save_and_play(self):
          # Save the audio generated.
          self.gtss_obj.save('audio/assistant_response.mp3')

          #Play the audio in the audio handler module:
          self.audio_handler_obj.play_audio('audio/assistant_response.mp3')


