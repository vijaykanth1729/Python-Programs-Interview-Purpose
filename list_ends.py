'''
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
the first and last elements of the given list.
For practice, write this code inside a function.
'''
new_list = []
def list_ends(my_list):
    first_value = my_list[0]
    last_value = my_list[-1]
    print("Original List: ",my_list)
    new_list.extend([first_value, last_value])
list_ends([5, 10, 15, 20, 25])
print("First and last values from original List: ", new_list)
