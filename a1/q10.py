print("To find the first 10 numbers of a geometric series")
ft = int(input("Enter the first term of the series\t"))
r = int(input("Enter the common ratio of the series\t"))
c = 0
while c!=10 :
	num = ft*(r**c)
	print (num)
	c = c + 1
