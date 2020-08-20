character_names = ('anna', 'amma', 'ayyya', 'chinnu','vijaykanth')
# find the longest name in character_names

longest_name = character_names[0]
index = 0

while index < len(character_names):
    if len(longest_name) < len(character_names[index]):
        longest_name = character_names[index]
    index+=1
print("The longest name is :", longest_name)
