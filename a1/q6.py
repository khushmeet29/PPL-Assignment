print("To find the first 10 pairs of amicable numbers")
def sum_of_divisors(n) :
	sum = 0
	for i in range (1, n):
		if(n % i == 0) :
			sum = sum + i
		i += 1
	return sum


num1 = 1
count = 0
while count != 10 :
	
		num2 = sum_of_divisors(num1)
		if (num1 < num2): 
			num3 = sum_of_divisors(num2)
			if (num3 == num1) :
				print(num1, num2)
				count += 1
		num1+=1

