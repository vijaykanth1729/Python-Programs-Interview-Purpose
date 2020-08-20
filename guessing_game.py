'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number,
then tell them whether they guessed too low, too high,
or exactly right. (Hint: remember to use the user input lessons
from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken,
and when the game ends, print this out.
'''
import random
random_num = random.randint(1,9)
print(random_num)
guesses = 0
while True:
    number = int(input("Enter a number: "))
    guesses+=1
    if number < random_num:
        print("You gueesed too low!!")
    elif number > random_num:
        print("You guessed too high!!")
    elif number == random_num:
        print("You guessed it correct!!")
        check = input("Do you want to exit now?, press 'YES' or 'NO' ")
        if check.lower()=='yes':
            print(f"Number of guesses you took is: {guesses}")
            break
        else:
            print("Keep Going.....")
            continue
