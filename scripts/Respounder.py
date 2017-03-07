import pyttsx

class Respounder():
    def respound(self, say):
        self.say = say
        engine = pyttsx.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(say)
        engine.runAndWait()