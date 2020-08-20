'''import random
a = random.sample(range(1,20), 11)
b = random.sample(range(1,30), 5)
print(a)
print(b)
-----------------------
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
'''
number = int(input("Enter a number!: "))
if number>2:
    for i in range(2, number):
        if number%i == 0:
            print(number,"Its not a prime number")
            break
    else:
        print(number,"is prime number!!")
else:
    print("Please enter a number which is more then 2..")
