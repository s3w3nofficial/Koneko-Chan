from OS_PathManager import *
from playsound import playsound

class MusicPlayer():
    def play_music(self, sound):
        self.sound = sound
        print "playing song: " + sound
        playsound(sound)
    
#MusicPlayer().play_music("C:\Users\kyber\Desktop\Koneko-chan\Koneko-Chan\scripts\TEST.mp3")