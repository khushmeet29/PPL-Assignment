#Raising and Handling Exceptions

#Example 1
print ("Example 1")
try:
	f1 = open("testfile1", "w")
	f1.write("This is my test file")
except IOError:
	print ("Error: can\'t find the file or read data")
else:
	print ("Written content in the file successfully")
	f1.close()
   
#Example 2
print ("Example 2")
try:
	f2 = open("testfile2", "r")
	f2.write("This is my test file")
except IOError:
	print ("Error: can\'t find file or read data")
else:
	print ("Written content in the file successfully")
	f2.close()

#Example 3
print ("Example 3")
while True:
	try:
		x = int(input("Please enter a number: "))
		break
	except ValueError:
		print ("That was not a valid number. Pls try again")

#Example 4
print("Example 4")
try:
	a = input("Enter Numerator: ")
	b = input("Enter Denominator: ")
	c = int(a)/int(b)
	print(c)
except ZeroDivisionError:
	print("Error:Denominator cannot be 0")

#Example 5
print("Example 5")
a = [1,2,3]	
try:
		print (a[4])
except IndexError:
	print("Error:list index out of range")
	




















