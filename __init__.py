# -*- coding: utf-8 -*-

from scripts.Parser import *
from scripts.Social import *
from scripts.ActionChosser import *
from scripts.Actions import *
from scripts.Respounder import *
from scripts.wikiScrapper import *

import speech_recognition as sr
#import pyttsx
import os
import sys
#import subprocess
#import wptools
import random

class speechRec():
    def listen_and_recognize(self):
        sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening!!!:")
            audio = sr.Recognizer().listen(source)
        try:
            speech = sr.Recognizer().recognize_google(audio, language="en")
            print("You said: " + speech)
            return speech
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return 'error'
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return 'error'
    
class news():
    def get_news(self):
        pass

class weather():
    def get_weather(self):
        pass
        
class MusicPlayer():
    def play_music(self):
        pass

if __name__ == "__main__":
    while True:
        ActionChosser().chosser(main_parser().parse_rec(speechRec().listen_and_recognize())) #parse some text
        #ActionChosser().chosser(main_parser().parse_rec("search for car"))