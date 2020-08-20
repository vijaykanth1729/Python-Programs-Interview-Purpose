'''
factorial can be  found by using the below equation..
n! = n*(n-1)*(n-2)*(n-3)....3.2.1
that means we can write this in below format..
n! = n*(n-1)!  where n>=1
if n=0 tha factorial value is 1..
'''

def factorial(n):
    if n>=1:
        return n*factorial(n-1)
    else:
        return 1

print(factorial(int(input("Enter a value to know factorial of it: "))))

# class Factorial:
#
#     def fact(self,n):
#         if n == 0:
#             return 1
#         else:
#             return n*self.fact(n - 1)
#
#
# f1 = Factorial()
# print(f1.fact(6))
