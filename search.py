search = input("What date would you like to search for?  >  ")
searchfile = open("reading.txt", "r")
for line in searchfile:
	if search in line: print(line)
searchfile.close()
