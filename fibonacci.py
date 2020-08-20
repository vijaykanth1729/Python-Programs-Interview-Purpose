'''
Write a program that asks the user how many Fibonnaci numbers to
generate and then generates them.
The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of the previous The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13,
two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …
'''
number = int(input("Enter a number of fibonnaci series you want: "))
n1, n2 = 0, 1
count = 0
if number<=0:
    print("Please enter a positive number which is greater then zero.")
elif number==1:
    print("Fibonacci sequence upto",number,":")
    print(n1)
else:
    while count<number:
        print(n1)
        n1,n2=n2,n1+n2
        count+=1

'''
using list comprehesnion
'''
series=[]
series.append(1)
series.append(1)
[series.append(series[k-1]+series[k-2]) for k in range(2,100)]

print(series)
