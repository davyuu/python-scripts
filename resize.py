import os
import sys
from PIL import Image

path  = os.getcwd()
oldPath = path+"\\hymn_image"
newPath = path+"\\new_hymn_image"
factor = 1/3
if not os.path.exists(newPath):
    os.makedirs(newPath)
filenames = os.listdir(oldPath)
for filename in filenames:
	filePath = os.path.join(oldPath, filename)
	im = Image.open(filePath)
	w, h = im.size
	newIm = im.resize((int(w*factor), int(h*factor)))
	newIm.save(newPath+"\\"+filename)
	
	