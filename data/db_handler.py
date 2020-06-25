'''Module to connect and handle the database'''

import sqlite3 as sql

class Db_Handler:
      def __init__(self):
          try:
              self.connection = sql.connect('data/database.db')
          except:
              pass

      def get_conn(self):
          return self.connection
