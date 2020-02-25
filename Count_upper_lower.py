
def words(str):
	count={"upper":0,"lower":0}



	for char in str:
		if char.isupper():
			count["upper"]+=1
		elif char.islower():
			count["lower"]+=1
		else:
			pass
	print("mecatar:",count["upper"],"poqratar:",count["lower"])


str=input("your full name: ")
words(str)