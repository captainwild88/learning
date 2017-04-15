name = input("What is you name sir? > ")
age = input("What is you age? > ")
username = input("What is you reddit username? > ")

print("So your name is %r you  are %r and your reddit username is %r"%(name, age, username))
with open("info.txt", "w") as text_file:
	text_file.write("So your name is %r you  are %r and your reddit username is %r"%(name, age, username))
