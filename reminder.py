'''User reminder module'''

import schedule
import time
import date_time_handler as dth
from data import db_handler as dbh


class Reminder:
      def __init__(self):
          self.conn = dbh.Db_Handler().get_conn()

      def set_new_task(self, date_time, task):
          try:
              self.conn.cursor().execute(''' INSERT INTO reminder(date, task) VALUES(?,?) ''', (date_time, task))
              self.conn.commit()
              self.conn.close()

          except Exception as e:
              print("Something is wrong, try again!\n")
              print(e)

      def remind_task(self):
          pass

#r = Reminder()
#r.set_new_task('24 abril','Remember me eat all food')