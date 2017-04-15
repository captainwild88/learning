import random

guess = input("Would you like to guess a number?  > ")

roll = random.randint(0,100)

while guess == roll:
	print("you guessed right")
else: print("Please try again the correct number was  "  + str(roll))	
