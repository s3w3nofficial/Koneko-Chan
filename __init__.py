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
import threading
         
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
        
def main():
    while True: 
        #ActionChosser().chosser(main_parser().parse_rec(speechRec().listen_and_recognize())) #parse some text
        ActionChosser().chosser(main_parser().parse_rec("play music"))
        #Respounder().respound("The quick brown nigga jumped over the lazy lukas")
        #Respounder().respound(other().read_content_from_text_file("bible.txt"))
        #MusicPlayer().play_all()
        
if __name__ == "__main__":
    #t = threading.Thread(target=get_url, args = (q,u)) thread with args
    t = threading.Thread(target=main())
    t.daemon = True
    t.start()