num=int(input("Enter some number"))



def number(int):
	
		if num==1:  
			
			return "Not prime"
		elif num==2:
			
			return "Prime"
		else:
			for i in range(2,num):
				if num%i==0:
					return "Not prime"
			return "prime"
print(number(int))		






