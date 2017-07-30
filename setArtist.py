import os
from mutagen.easyid3 import EasyID3
path  = os.getcwd()
filenames = os.listdir(path)
for filename in filenames:
	if(filename.endswith(".mp3")):
		nameWithMp3 = filename.split("-")[1].strip()
		name = nameWithMp3.split(".")[0].strip()
		print(name)
		audio = EasyID3(filename)
		audio['title'] = name
		audio['artist'] = u""
		audio['album'] = u"Shigatsu wa Kimi no Uso"
		audio.save()