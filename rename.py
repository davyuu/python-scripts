import os
path  = os.getcwd()
filenames = os.listdir(path)
for filename in filenames:
	split = filename.split('.')
	if(len(split) > 2):
		newfilename = 'Shigatsu wa Kimi no Uso -' + split[1].title() + '.' + split[2]
		print(newfilename);
		os.rename(os.path.join(path, filename), os.path.join(path, newfilename))
