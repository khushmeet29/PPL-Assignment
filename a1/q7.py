print("To find Armstrong Numbers in a given range")
l = int(input("Enter lower limit of the range\t"))
u = int(input("Enter upper limit of the range\t"))
list1 = []
for num in range(l, u+1):
	temp = num
	sum = 0
	while temp > 0 :
		mod = temp % 10
		sum += mod**3
		temp //= 10
	if num==sum:
		list1.append(num)
if(len(list1)!=0) :
	print("The Armstrong numbers are\t", list1)
else :
	print("There are no Armstrong numbers in the given range")



