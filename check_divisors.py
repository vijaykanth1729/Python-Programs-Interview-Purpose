number = int(input("Enter a number to check all of its divisors.."))
all_divisors = []
for i in range(2,11):
    if number % i == 0:
        all_divisors.append(i)
print(f"for this given number: {number}, these are available divisors--> {all_divisors}")
