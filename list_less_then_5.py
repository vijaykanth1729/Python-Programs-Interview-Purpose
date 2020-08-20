a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,4]
new_list = []
for i in a:
    if i<5:
        new_list.append(i)

print(new_list)
'''
doing by list comprehension
'''

my_comprehension = [i for i in a if i<5]
print(my_comprehension)

number = int(input("Please enter a number: "))
data = [i for i in a if i<number] # returns a new_list with the numbers which are less then user entered input from a
print(data)
