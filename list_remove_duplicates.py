'''
Write a program (function!) that takes a list and returns a new
list that contains all the elements of the first list minus all the duplicates.
Extras:

Write two different functions to do this - one using a loop and constructing a
list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a
different function.
'''
original = []
def remove_duplicates(my_list):
    print("Original data: ", my_list)
    data = set(my_list)
    original.append(data)

def using_loop(my_list):
    y = []
    for i in my_list:
        if i not in y:
          y.append(i)
    print("Using loop to remove duplicates: ",y)

remove_duplicates([1,2,3,4,5,4,2])
using_loop([1,2,3,4,5,4,2])
print("Using set function to remove duplicates:", original)
