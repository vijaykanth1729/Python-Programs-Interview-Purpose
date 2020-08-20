'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''
'''
data = input("Please enter a string: ")
if data[0:] == data[::-1]:
    print("This is a palindrome")
else:
    print("Invalid palindrome")
'''
def palindrome_check(string)->str:
    x = ''
    for i in range(len(string)):  # string: ram (0,1,2)
        x+=string[len(string)-1-i]  # string[3-1-i] #i=0 string[2] mar
    print(x)
    return x
word = input("Enter a word: ")
if word == palindrome_check(word):
    print("This is a palindrome")
else:
    print("Not a palindrome")
