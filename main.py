if __name__=="__main__":
   import speech
   import tasks

   sp = speech.Speech()
   sp.get_speech()
   task = tasks.Task()
   task.run_task()
