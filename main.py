if __name__=="__main__":
   import speech
   import tasks
   import audio_handler

   audio = audio_handler.Audio()
   sp = speech.Speech()
   task = tasks.Task()

   audio.greet()
   sp.get_speech()
   task.run_task()
