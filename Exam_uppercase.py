

# 4.Write a Python class which has two methods get_String and print_String.
#  get_String accept a string from the user and print_String print the string in upper case.


# "գրիր կլաս, որը ունի 2 մեթոդ՝ get_string ու print_string.
# Get_string-ն ընդունում է սթրինգ օգտագործողից, իսկ print_string-ը տպում է սթրինգը՝ մեծատառերով"

name=input("What is your name? ")
class Uppercase:
	# self.name=input()

	def	get_string(self):
		self.name=name

	def print_string(self):
		print (name.upper())

# print(Uppercase().name.upper())


printed=Uppercase()
printed.get_string()
printed.print_string()

