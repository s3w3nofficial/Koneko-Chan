import os

class OS_PathManager():
    def get_music_path(self):
        files = os.listdir("D:")
        print len(files)
        i = len(files) - 1
        while i != -1:
            if "mp3" not in files[i]:
                files.pop(i)
            else:
                a = files[i]
                files[i] = "D:\\" + a
                print a
            i -= 1
        for file in files:
            print len(files)
        return files

OS_PathManager().get_music_path()   