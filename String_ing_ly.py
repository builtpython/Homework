


string=input("Please write me a word :")

if len(string)<3:
	print(string)
else:

	if string.endswith("ing"):
		print(string+"ly")
	else: 
		print(string+"ing")


