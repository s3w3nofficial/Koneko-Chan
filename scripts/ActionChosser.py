from Actions import *

class ActionChosser():
    def chosser(self, call):
        self.call = call
        if call[0] == '0':
            Actions().search(call[1])
        elif call[0] == '1':
            Actions().run_process(call[1])
        elif call[0] == '2':
            pass
        if call[0] == '3':
            Actions.PlayMusic(call[1])
        """
        elif call[0] == '3':
            Actions().social(call[1])
        """