import os

class OS_PathManager():
    def get_music_path(self):
        files = os.listdir("D:") #get all files from D:
        print len(files)
        i = len(files) - 1 
        #remove all files that dont contains mp3 using backward for cycle
        while i != -1:
            if "mp3" not in files[i]: 
                files.pop(i)
            else:
                a = files[i]
                files[i] = "D:\\" + a
                print a
            i -= 1
        #print all files
        for file in files:
            print file
        #retun files
        return files

#OS_PathManager().get_music_path()   