import winsound

class MusicPlayer():
    def play_music(self, sound):
        self.sound = sound
        winsound.PlaySound(sound, winsound.SND_FILENAME)