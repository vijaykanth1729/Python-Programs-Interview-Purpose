my_dict = {}
with open('abc.txt', 'r') as f:
    for line in f:
        (key, value) = line.split()
        my_dict[key] = value
    for key, value in my_dict.items():
        print(key, value)
