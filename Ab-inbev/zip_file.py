from zipfile import ZipFile, ZIP_DEFLATED

f = ZipFile('files7.zip', 'w',ZIP_DEFLATED)
f.write('abc.txt')
f.write('file1.txt')
f.close()
print("files7.zip  creation success..")
