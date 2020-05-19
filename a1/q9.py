print("To find the first 10 harmonic divisor numbers")
i = 1
sum = 0
count = 0
num = 1
z = 0
while z != 10 :
	i = 1
	sum = 0
	count = 0
	hm = 0
	while i <= num:
		if ((num % i) == 0) :
			sum += (1/i)
			count = count + 1
		i = i + 1
	hm = count/sum;
	if ((hm - int(hm)) == 0) :
		print(num)
		z = z + 1
	num = num + 1

	

			
