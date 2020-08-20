from zipfile import ZipFile, ZIP_STORED

f = ZipFile('files7.zip', 'r', ZIP_STORED) # for performing unzip operation..
names = f.namelist()
print(names)
print('')
for name in names:
    print('FileName: ',name)
    print('The content of this file: ')
    f1 = open(name, 'r')
    print(f1.read())
    print('*'*10)
