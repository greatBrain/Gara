'''User reminder module'''

import schedule
import time
import date_time_handler as dth
from data import db_handler as dbh


class Reminder:
      def __init__(self):
          self.conn = dbh.Db_Handler().get_conn()
          self.cursor = self.conn.cursor()
          self.dth = dth.Date_And_Time()

          self.task = ''

      def set_new_task(self, date, hour, task):
          try:
              self.cursor.execute(''' INSERT INTO reminder(date, hour, task) VALUES(?,?,?) ''', (date, hour, task))
              self.conn.commit()
              print("Agregado!")

          except Exception as e:
              print("Something is wrong, try again!\n")
              print(e)


      def remind_task(self):
          schedule.every(3).seconds.do(self.get_task)

          while True:
              schedule.run_pending()
              time.sleep(1)

      def get_task(self):
          for i in self.cursor.execute("SELECT * FROM reminder"):
              #self.rowid = i[0]

              if i[0] == self.dth.get_date():
                 if self.dth.get_time() == i[1]:
                    self.task = i[2]
                    self.task_to_speech(self.task)
                    #Then, call the function that deletes tha task from dabase:
                    #self.delete_task()
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


r = Reminder()
dth = dth.Date_And_Time()
#r.set_new_task('2020-06-26', '20:29', 'this is only a joke. trying the assistance')
r.remind_task()