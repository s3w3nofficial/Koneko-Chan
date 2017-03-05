from scripts.Respounder import *
from scripts.wikiScrapper import *
import subprocess

class Actions():
    def search(self, name):
        self.name = name
        wiki().wiki_search(name)
    def run_process(self, name):
        self.name = name
        Respounder().respound("running porcess name " + name)
        subprocess.call('C:\Windows\\system32\\' + name + '.exe')
    def alarm(self, time): #get time as 01:20:PM
        self.time = time
        #convert time to second an set alarm
        time_array = time.split(":")
        alarm_time = 0
        if time_array[2] == 'PM':
            a = time_array[0]
            b = 12 + int(a)
            time_array[0] = str(b)
        time_array.pop(2)
        alarm_time += int(time_array[0]) * 3600
        alarm_time += int(time_array[1]) * 60
        #TODO set alarm
        
    def social(self, social):
        self.social = social
        Social().social(social)