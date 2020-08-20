import csv
with open('marks.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['NAME', 'ID-NUMBER', 'MARKS', 'ADDRESS'])
    while True:
        name = input("Enter your Name: ")
        id_number = input("Enter your Id_Number: ")
        marks = input("Enter your Marks: ")
        address = input("Enter your Address: ")
        w.writerow([name, id_number, marks, address])
        another_data = input("Do you want to insert one more record [YES|NO] ")
        if another_data.lower() == 'no':
            break
