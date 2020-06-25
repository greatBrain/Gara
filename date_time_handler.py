'''Module to handle the time and the dates, as an interface'''
import time
from datetime import datetime

class Date_And_Time:
      def __init__(self):
          pass

      def get_time(self):
          self.time = time.localtime(time.time())
          self.current_time = time.strftime("%H:%M:%S", self.time)

          return self.current_time

      def get_date(self):
          return datetime.today().strftime('%Y-%m-%d')

      def get_date_and_time(self):
          return datetime.today().strftime('%Y-%m-%d-%H:%M')


Date_And_Time().get_date_and_time()

