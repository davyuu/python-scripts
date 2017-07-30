import os
import shutil
path  = os.getcwd()
songs = path+'/songs'
foldernames1 = os.listdir(path)
for foldername1 in foldernames1:
	if foldername1.endswith('mp3'):
		foldernames2 = os.listdir(path+'/'+foldername1)
		for foldername2 in foldernames2:
			filenames = os.listdir(path+'/'+foldername1+'/'+foldername2)
			for filename in filenames:
				filepath = path+'/'+foldername1+'/'+foldername2+'/'+filename
				print(filepath)
				shutil.copy2(filepath, songs)