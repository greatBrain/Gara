'''Tasks module and handler'''

import re
import subprocess as subp
import webbrowser as wbb
import requests
from requests.exceptions import MissingSchema
from speech import Speech
from text_to_speech import Text_To_Speech
import date_time_handler as dth
import reminder


class Task:
    def __init__(self):
        self.user_speech = Speech().get_speech()
        self.assistant_call = str(self.user_speech)

        self.HTTP = "http://www."
        self.HTTPS = "http://www."

        self.domains = ['.com', '.org',
                        '.net', '.es'
                        ]

        self.ASSISTANT_NAME = 'alexa'

        self.COMMANDS = {'application':'aplicacion',
                         'web': 'web',
                         'time':'hora',
                         'date':'fecha',
                         'date and time':'fecha y hora',
                         'schedule':'agenda'
                         }

    def run_task(self):
        try:
            if re.match(self.assistant_call, self.ASSISTANT_NAME):
               Text_To_Speech().translate_and_play("Hola, como puedo ayudarte?")

               self.command = Speech().get_speech()
               str(self.command)

               for eng, esp in self.COMMANDS.items():
                   if self.command==eng or self.command==esp:
                      self.say_time()

        except Exception as e:
             print("Invalid command\n")
             print(e)

    def open_web(self, web_name):

        try:
            self.stop = False

            while self.stop:
                for dom in range(len(self.domains)):
                    self.website = (self.HTTPS + web_name + self.domains[dom])
                    self.request = requests.get(self.website)

                    if self.request:
                        wbb.open(self.website)
                        self.stop = True
                    else:
                        continue

        except MissingSchema as m:
            print("The provided URL is invalid. Try again!\n")
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


