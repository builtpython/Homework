# 2. Write a Python class to implement pow(x, n).


# class py_solution:
#    def pow(self, x, n):
#         if x==0 or x==1 or n==1:
#             return x 

#         if x==-1:
#             if n%2 ==0:
#                 return 1
#             else:
#                 return -1
#         if n==0:
#             return 1

#         if n<0:
#             return 1/self.pow(x,-n)

#         num = self.pow(x,n//2)
#         if n%2 ==0:
#             return num*num
#         return num*num*x

# print(py_solution().pow(2, -3));
# print(py_solution().pow(3, 5));
# print(py_solution().pow(100, 0))




# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if(n==1):
#             return x
#         if(x==0 and n<=0):
#             return
#         if(n==0):
#             return 1
#         if(n<0):
#             return 1/self.myPow(x,-n)
#         p = self.myPow(x, n//2)
#         ret = p*p
#         if(n%2 == 1):
#             return ret*x
#         return ret







x = int(input("Choose a base number from -100 to 100"))
n = int(input("Choose an exponent number from -10 to 10"))
class Power:
   
    def pow(self, x,n):
        return x**n

print(Power().pow(x,n))

