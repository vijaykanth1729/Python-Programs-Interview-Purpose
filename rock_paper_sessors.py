import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1==u2:
        return "Its a Tie"
    elif u1=="rock":
        if u2=="scissors":
            print("Rock wins!!")
        else:
            print("scissors wins!!")
    elif u1=="scissors":
        if u2=="paper":
            print("scissors wins!")
        else:
            print("paper wins!!")
    elif u1=="paper":
        if u2=="rock":
            print("Paper wins!!!")
        else:
            print("rock wins!!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")

data=compare(user1_answer, user2_answer)
print(data)


# print('''Please pick one:
#             rock
#             scissors
#             paper''')
#
# while True:
#     game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
#     player_a = str(input("Player a: "))
#     player_b = str(input("Player b: "))
#     a = game_dict.get(player_a)
#     b = game_dict.get(player_b)
#     dif = a - b
#
#     if dif in [-1, 2]:
#         print('player a wins.')
#         if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
#             continue
#         else:
#             print('game over.')
#             break
#     elif dif in [-2, 1]:
#         print('player b wins.')
#         if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
#             continue
#         else:
#             print('game over.')
#             break
#     else:
#         print('Draw.Please continue.')
#         print('')
