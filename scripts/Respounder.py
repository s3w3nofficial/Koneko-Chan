import pyttsx

class Respounder():
    def respound(self, say):
        self.say = say
        engine = pyttsx.init()
        engine.say(say)
        engine.runAndWait()