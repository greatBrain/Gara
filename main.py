if __name__=="__main__":
   import speech
   import warnings as war
   war.filterwarnings('ignore')

   sp = speech.Speech()
   sp.get_speech()
   sp.run_command()
