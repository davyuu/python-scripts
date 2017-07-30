import urllib
htmlfile = urllib.urlopen("http://allrecipes.com")
htmltext = htmlfile.read()
print(htmltext)