print("To find the missing page numbers of a 25 page book")
list1 = eval(input("Enter the list of page numbers present\t"))
list2 = []
flag = 0
i = 0
for i in range(1, 26) :
	flag = 0
	for j in list1 :
		if (i == j) :
			flag = 1
			break
	if (flag == 0) :
		list2.append(i)
	i=i+1
print ("The missing page numbers are\n")
print (list2)

			
				  
