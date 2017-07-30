print("Hello World")
myName = input("What is your name?")
count = 0
for x in range(len(myName)-1,-1,-1):
	print(myName[x] + ": " + myName[count])
	var = myName[count]
	myName[count] = b
	myName[x] = var
	count = count + 1
print(myName)
input("Enter to Exit")
