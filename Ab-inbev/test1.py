import os
os.chdir('Testing')
extension = ''
count = 0
while True:
    if extension == '':
        my_file = input("Enter a filename: ")+'.txt'
    else:
        my_file = input("Enter a filename: ")+extension
    count+=1
    with open(my_file, 'wb') as f:
        pass
        if count==3:
            break
print("Data saved Succesfull")
