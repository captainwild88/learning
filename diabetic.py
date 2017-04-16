from datetime import datetime
import sys

datestring = datetime.strftime(datetime.now(), '%d/%m/%Y_%H:%M:%S')
reading = str(input("What is your reading:  "))
f = open("reading.txt", 'a')
f.write("%r %r" % (reading, datestring))
f.write("\n")
f.close()


if reading <= "3.5":
	print("reading to low")
elif reading >= "4.5":
	print("reading to high")
else:
	print("reading within range")
	
