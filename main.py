if __name__=="__main__":
   from speech import Speech
   from tasks import Task
   #import audio_handler

   #audio = audio_handler.Audio()
   sp = Speech()
   task = Task()

   sp.get_speech()
   task.run_task()
