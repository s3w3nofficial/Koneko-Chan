from Actions import *
from MusicPlayer import *

class ActionChosser():
    def chosser(self, call):
        self.call = call
        if call[0] == '0': #search chosser
            Actions().search(call[1])
        elif call[0] == '1': #run_process
            Actions().run_process(call[1]) 
        elif call[0] == '2': #set alarm
            pass
        elif call[0] == '3': #music player
            print call[1]
            Actions().PlayMusic(call[1])
        """
        elif call[0] == '3': #social
            Actions().social(call[1])
        """