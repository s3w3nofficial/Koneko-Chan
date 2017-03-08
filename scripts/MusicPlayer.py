from OS_PathManager import *
from playsound import playsound

class MusicPlayer():
    def play_music(self, sound):
        self.sound = sound
        print "playing song: " + sound
        playsound(sound)
    def play_all(self):
        stack = OS_PathManager().get_music_path()
        for s in stack:
            print s
        for s in stack:
            playsound(s)
  
#MusicPlayer().play_music("C:\Users\kyber\Desktop\Koneko-chan\Koneko-Chan\scripts\TEST.mp3")
#MusicPlayer().play_all()