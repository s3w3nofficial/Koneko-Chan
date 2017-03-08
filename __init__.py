# -*- coding: utf-8 -*-

from scripts.Parser import *
from scripts.Social import *
from scripts.ActionChosser import *
from scripts.Actions import *
from scripts.Respounder import *
from scripts.wikiScrapper import *
from scripts.MusicPlayer import *
from scripts.OS_PathManager import *
from scripts.VoiceRec import *

#import speech_recognition as sr
#import pyttsx
import os
import sys
#import subprocess
#import wptools
import random
import time
import thread

class Thread():
   #def myThread(self, threadName, delay):
   def print_time( threadName, delay):
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            print "%s: %s" % ( threadName, time.ctime(time.time()) )
         
""""    
class news():
    def get_news(self):
        pass

class weather():
    def get_weather(self):
        pass
"""

class other():
    def read_content_from_text_file(self, name):
        self.name = name
        r = open(name)
        print r.read()
        return r.read()

if __name__ == "__main__":

    # Create two threads as follows
    try:
        thread.start_new_thread( Thread().print_time, ("Thread-1", 2, ) )
        thread.start_new_thread( Thread().print_time, ("Thread-2", 4, ) )
    except:
        print "Error: unable to start thread"
    """
    while True: 
        #ActionChosser().chosser(main_parser().parse_rec(speechRec().listen_and_recognize())) #parse some text
        #ActionChosser().chosser(main_parser().parse_rec("search for car"))
        #Respounder().respound("The quick brown nigga jumped over the lazy lukas")
        #Respounder().respound(other().read_content_from_text_file("bible.txt"))
        #MusicPlayer().play_all()
    """

    while 1:
        pass