# -*- coding: utf-8 -*-

import speech_recognition as sr
import pyttsx
import os
import subprocess
import wptools
import random

social_grammer = ['how are you', 'do you like kkk']

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

class Respounder():
    def respound(self, say):
        self.say = say
        engine = pyttsx.init()
        engine.say(say)
        engine.runAndWait()

class main_parser():
    def parse_rec(self, text):
        self.text = text
        social_text = text
        text = text.split(' ')

        call = []
        i = 0
        for word in text:
            if word == 'search':
                call.append('0')
            elif word == 'open' or word == 'run':
                call.append('1')
                call.append(text[i+1].lower())
                break
            elif word == 'wake' or word == 'set alarm':
                call.append('2')
                break

    #search parser
            if word == 'for':
                #append everithink next
                i += 1
                while i < len(text):
                    if len(text) - 1 == i:
                        call.append(text[i]) #dont add space to last word of array    
                    else:
                        call.append(text[i] + " ")
                    i += 1
            i += 1
        
        #check for social
        for social in social_grammer:
            print social_text, social
            if social_text == social:
                call.append('3')
                call.append(social_text.lower())
            break

        #merge strings after for
        if len(call) > 2:
            call[1:len(call)] = [''.join(call[1:len(call)])]
            print call[1]
        print call[0]
        return call #return call

class ActionChosser():
    def chosser(self, call):
        self.call = call
        if call[0] == '0':
            Actions().search(call[1])
        elif call[0] == '1':
            Actions().run_process(call[1])
        elif call[0] == '2':
            pass
        elif call[0] == '3':
            Actions().social(call[1])

class wiki():
    def wiki_search(self, query):
        self.query = query
        query = wptools.page(query).get_wikidata()
        try: 
            query = query.wikidata['description']
        except:
            Respounder().respound("Error query not found")

        Respounder().respound("I find thease informations about your request" + query)
    
class news():
    def get_news(self):
        pass

class weather():
    def get_weather(self):
        pass
        
class MusicPlayer():
    def play_music(self):
        pass

class Social():
    def social(self, social):
        self.social = social
        i = 0
        while i < len(social_grammer):
            if social == social_grammer[i]:
                Social().social_response(i)
                break
            i += 1
    def social_response(self, i):
        self.i = i
        if i == 0:
            rnd = random.randint(0, 2)
            respone = ['im fine thank you', 'it is little hot today', 'im ok']
            Respounder.respound(respone[rnd])
        elif i == 1:
            rnd = random.randint(0, 1)
            respone = ['yes i do', 'kkk is best']
            Respounder.respound(respone[rnd])

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

if __name__ == "__main__":
    while True:
        ActionChosser().chosser(main_parser().parse_rec(speechRec().listen_and_recognize())) #parse some text