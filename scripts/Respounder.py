import pyttsx
"""
class Respounder():
    def respound(self, say):
        self.say = say
        engine = pyttsx.init()
        engine.say(say)
        engine.runAndWait()
"""
class Respounder():
    def respound(self, say):
        self.say = say
        engine = pyttsx.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            engine.setProperty('voice', voice.id)
            engine.say(say)
        engine.runAndWait()