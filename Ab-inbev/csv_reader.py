import csv
f = open('marks.csv', 'r')
r = csv.reader(f)
data = list(r)
if 'vijay' in data[1][0]:
    data[1][0] = '****'
else:
    pass
f1 = open('marks1.csv', 'w', newline='')
w = csv.writer(f1)
w.writerow(data)
for row in data:
    for column in row:
        print(column, '\t', end='')
