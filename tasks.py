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
        self.user_command = Speech().get_command()

        self.HTTP = "http://www."
        self.HTTPS = "http://www."

        self.domains = ['.com', '.org',
                        '.net', '.es'
                        ]

        self.commands = {'application':'aplicación',
                         'web': 'web',
                         'time':'hora',
                         'schedule':'agenda'
                         }

    def run_task(self):
        try:
           # Split the text to get a command
           self.text_splited = re.split(' ', self.user_command)

           for eng, esp in self.commands.items():
               for i in range(len(self.text_splited)):
                   if re.search(eng, self.text_splited[i]) or re.search(esp, self.text_splited[i]):

                       if eng == 'application' or esp == 'aplicación':
                            self.open_app(self.text_splited[i + 1])

                       elif eng == 'web' or esp == 'web':
                            self.open_web(self.text_splited[i + 1])

                       elif eng == 'time' or esp == 'hora':
                            self.say_time()
                       else:
                           pass
                   else:
                      Text_To_Speech().translate('Sorry, something is wrong.. Try it again!')
                      Text_To_Speech().save_and_play()

        except Exception as e:
            print("Invalid command. Please check the commands list!\n")
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
        Text_To_Speech().translate(dth.Date_And_Time().get_time())
        Text_To_Speech.save_and_play()

    def say_date(self):
        Text_To_Speech().translate(dth.Date_And_Time().get_date())
        Text_To_Speech.save_and_play()

    def say_date_time(self):
        Text_To_Speech().translate(dth.Date_And_Time().get_date_and_time())
        Text_To_Speech.save_and_play()


