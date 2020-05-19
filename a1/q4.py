import random
val = random.randint(1,100)
print ("You get 5 chances to guess the number")
count = 5	
flag = 0
while count != 0 :
	inp = int(input("enter a number\t"))
	if (inp>val) :
		print ("Entered number is greater than the number to be guessed")
	elif (inp<val) :
		print("Entered number is lesser than the number to be guessed")
	else :
		print("Congratulations! You guessed the number!!")
		flag = 1
		break
	count=count-1
if (flag == 0) :
	print ("Sorry, You couldn't guess the number, the correct number is ", val)


	

