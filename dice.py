import random
#from random import randint
min_throw = 1
max_throw = 6

roll_dice = input("Roll dice?  >  ")

roll_dice = "yes"

while roll_dice == "yes" or roll_dice == "y":
	print("rolling the dice...")
	print("you rolled...")
	print (random.randint(min_throw,max_throw))
	print (random.randint(min_throw,max_throw))
	break

again = input("Roll again? >  ")

while again == "yes" or again == "y":
	print("rolling the dice...")
	print("you rolled...")
	print (random.randint(min_throw,max_throw))
	print (random.randint(min_throw,max_throw))
	break
	
