list=[1,2,3,4,5,6,7,8]

def number(int):
	even=[]	
	for i in list:
		if i%2==0:
			even.append(i)
	return even
print(number(list))



