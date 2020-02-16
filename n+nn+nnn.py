# "4. Write a Python program that accepts an integer (n) and 
# computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615"




n=int(input("Choose a number between 1 and 9."))

def function(n):
	return n+(n*10+n)+(n*100+n*10+n)
print(function(n))





