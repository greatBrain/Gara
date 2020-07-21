'''Tasks module and handler'''

import re
import subprocess as subp
import webbrowser as wbb
import requests
from requests.exceptions import MissingSchema
from speech import Speech
from text_to_speech import Text_To_Speech
import date_time_handler as dth
from reminder import Reminder


class Task:
    def __init__(self):
        self.user_speech = Speech().get_speech()
        self.assistant_call = str(self.user_speech)

        self.HTTP = "http://www."
        self.HTTPS = "http://www."

        self.DOMAINS = ['.com', '.org',
                        '.net', '.es'
                        ]

        self.WAKE_WORD = 'francis'

        self.COMMANDS = {'application':'aplicacion',
                         'web': 'web',
                         'time':'hora',
                         'date':'fecha',
                         'date and time':'fecha y hora',
                         'schedule':'agenda'
                         }

    def run_task(self):
        try:
            if self.assistant_call in self.WAKE_WORD:
               Text_To_Speech().translate_and_play("Hola, como puedo ayudarte?")

               self.command = Speech().get_speech()
               str(self.command)

               self.command_splited = re.split(' ', self.command)

               for eng, esp in self.COMMANDS.items():
                   for i in range(len(self.command_splited)):
                        if self.command_splited[i] in self.COMMANDS:
                            if self.command_splited[i]=='web':
                                self.open_web(self.command_splited[i+1])

                            elif self.command_splited[i]=='application' or self.command_splited[i]=='applicacion':
                                 self.open_app((self.command_splited[i+1]))

                            elif self.command_splited[i]=='time' or self.command_splited[i]=='hora':
                                 self.say_time()

                            elif self.command_splited[i]=='schedule' or self.command_splited[i]=='agenda':
                                 for ask in self.ask_schedule_info:
                                     for data in self.send_schedule_data():
                                         Text_To_Speech().translate_and_play(ask)


        except Exception as e:
             print("Invalid command\n")
             print(e)    

    def set_task(self):
        Reminder().get_schedule_info()

    def open_web(self, web_name):

        try:
            self.stop = False

            while self.stop:
                for dom in range(len(self.DOMAINS)):
                    self.website = (self.HTTPS + web_name + self.self.DOMAINS[dom])
                    self.request = requests.get(self.website)

                    if self.request:
                        wbb.open(self.website)
                        self.stop = True
                    else:
                        continue

        except MissingSchema as m:
            print("URL is invalid. Try again!\n")
            raise m
        except Exception as e:
            raise e

    def open_app(self, app):
        try:
            subp.call(app)
        except Exception as e:
            print("Could not open or find the program. Try again!\n")
            raise e

    def say_time(self):
        Text_To_Speech().translate_and_play(dth.Date_And_Time().get_time())

    def say_date(self):
        Text_To_Speech().translate_and_play(dth.Date_And_Time().get_date())

    def say_date_time(self):
        Text_To_Speech().translate_and_play(dth.Date_And_Time().get_date_and_time())


