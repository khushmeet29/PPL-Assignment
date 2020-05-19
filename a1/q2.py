print("Dice Rolling Simulator")
import random
output = "yes"

while output == "yes":
	
	print("The number is\n")
	val = random.randint(1,6)
	print(val)
	output = input("do you want to roll the dice again?(Answer can be yes or no)")

