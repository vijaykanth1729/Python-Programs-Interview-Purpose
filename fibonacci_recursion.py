'''
fibonacci:

1 1 2 3 5 ....etc
Joining 1+1 gives 2, 2+3 gives 5 so on..
fn = fn-1+fn-2
f5 = f4+f3
if n>=3 above condition works..

'''

def fibonacci(n):
    # a = 0
    # b = 1
    # count = 0
    # if n==2:
    #     print(a,b)
    # elif n>=3:
    #     while count<n:
    #         a, b = b, a+b
    #         print(a)
    #         count+=1

    if n>=3:
        return fibonacci(n-1)+fibonacci(n-2)
    else:
        return 1
print(fibonacci(6))
