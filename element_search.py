'''
Write a function that takes an ordered list of numbers
(a list where the elements are in order from smallest to largest)
and another number. The function decides whether or not the
given number is inside the list and returns (then prints) an appropriate boolean.
'''
def element_search(ordered_list, number):
    if number in ordered_list:
        return True
    else:
        return False
if __name__=='__main__':
    ordered_list = [1,2,3,4,5,6,7,8]
    number = int(input("Enter a number to search: "))
    print(element_search(ordered_list, number))
