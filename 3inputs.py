
# Take 3 inputs from user and check : 1. all are equal 2. any of two are equal 


print("How many km can you run per day?")
a=input()
print("How many km do you run on average per day?")
b=input()
print("What is your desired daily record in km?")
c=input()

all = a==b and a==c and b==c 
print ("all are equal:", all)
any = a==b or b==c or a==c
print("any two results are equal:",any)


