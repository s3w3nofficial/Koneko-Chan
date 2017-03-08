import speech_recognition as sr
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