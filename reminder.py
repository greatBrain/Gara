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

      def set_new_task(self, date, hour, task):
          try:
              self.cursor.execute(''' INSERT INTO reminder(date, hour, task) VALUES(?,?,?) ''', (date, hour, task))
              self.conn.commit()
              #self.conn.close()
              print("Agregado!")

          except Exception as e:
              print("Something is wrong, try again!\n")
              print(e)


      def get_task(self):

          for i in self.cursor.execute("SELECT * FROM reminder"):
              if i[0] == self.dth.get_date():
                 if self.dth.get_time() == i[1]:
                    self.task = i[2]
                    print(self.task)
                 else:
                    return "Error to compare, index error!"
              else:
                 return "Error to compare the dates!"


      def remind_task(self):
          #schedule.every().hour.do(self.get_task())
          schedule.every(5).seconds.do(self.get_task)

          while True:
              schedule.run_pending()
              time.sleep(1)


r = Reminder()
dth = dth.Date_And_Time()
#r.set_new_task('2020-06-25', '17:33', 'Remember me eat all food')
r.remind_task()