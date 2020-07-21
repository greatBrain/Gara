'''User reminder module'''

import schedule
import time
import date_time_handler as dth
from data import db_handler as dbh
from text_to_speech import Text_To_Speech 
from speech import Speech

class Reminder:
      def __init__(self):
          self.conn = dbh.Db_Handler().get_conn()
          self.cursor = self.conn.cursor()
          self.date_time_handler = dth.Date_And_Time()

          self.task = ''

      #With this generator, The assistant will ask to create the schedule
      def get_schedule_info(self):
          questions = [
                    "Please, tell me the day?", 
                    "now, the exactly hour", 
                    "what would you like to remember?"
          ]
          
          schedule_data = []
          
          while True:
                for i, ask in enumerate(questions):
                    Text_To_Speech().translate_and_play(questions[i])
                    schedule_data.append(str(Speech().get_speech()))
                break
          self.set_new_task(schedule_data)

      def set_new_task(self, data):
          try:
              self.cursor.execute(''' INSERT INTO reminder(date, hour, task) VALUES(?,?,?) ''', (data[0], data[1], data[2]))
              self.conn.commit()
              Text_To_Speech().translate_and_play("Added susscesfully!")

          except Exception as e:
              Text_To_Speech().translate_and_play("Somthing is not right, please try again")
              #print(e)


      def remind_task(self):
          schedule.every(3).seconds.do(self.get_task)

          while True:
              schedule.run_pending()
              time.sleep(1)

      def get_task(self):
          for i in self.cursor.execute("SELECT * FROM reminder"):
              #self.rowid = i[0]

              if i[0] == self.date_time_handler.get_date():
                 if self.date_time_handler.get_time() == i[1]:
                    self.task = i[2]
                    self.task_to_speech(self.task)
                    #Then, call the function that deletes tha task from dabase:
                    #self.delete_task(rowid)
                 else:
                    return "Time out!"
              else:
                 return "Error in the dates!"


      def task_to_speech(self, task):
          import text_to_speech as ttsp
          self.ttsp = ttsp.Text_To_Speech(str(task))
          self.ttsp.translate()
          self.ttsp.save_and_play()

      def delete_task(self, rowid):
          self.cursor.execute("DELETE FROM reminder WHERE rowid=?", (rowid))


if __name__=="__main__":
   Reminder().get_schedule_info() 

#r = Reminder()
#dth = dth.Date_And_Time()
#r.set_new_task('2020-06-26', '20:39', 'this is a joke. i am the joker')
#r.remind_task()