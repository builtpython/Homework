# Take two numbers and check whether the sum is greater than 5, less than 5 or equal to 5.

first=int(input("How many meters far can you jump?"))
second=int(input("How many meters high can you jump?"))
sum=first+second


print ("Sum is greater than 5:", bool(sum > 5))
print ("Sum is equal to 5:", bool(sum == 5))
print ("Sum is lesser than 5:", bool(sum < 5))