a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

'''
write a program that returns a list that contains only the elements that are,
common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
'''
new_list = []
new_a  = set(a)
new_b = set(b)
for i in new_a:
    if i in new_b:
        new_list.append(i)
print(new_list)

'''
Using comprehension techniques..
'''
comprehension = [i for i in set(a) if i in set(b)]
print(comprehension)
