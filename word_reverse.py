'''
Write a program (using functions!) that asks the user for a long
string containing multiple words. Print back to the user the same string,
except with the words in backwards order. For example, say I type the string:

 My name is Michele
Then I would see the string:

 Michele is name My
'''
def my_func(my_string):
    '''reverse the word'''
    words =  my_string.split()
    reverse_words = words[::-1]
    #print(reverse_words)
    my_string = ' '.join(reverse_words)
    return my_string
print(my_func("My name is Michele"))
