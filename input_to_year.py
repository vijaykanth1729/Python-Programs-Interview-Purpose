from datetime import datetime
year=datetime.now().year
name = input("Enter Your Name: ")
print(f"Hello Mr.{name}")
age = int(input("How old are you: "))
new_data = str((year-age)+100)
print(f"{name} you will be 100 years old in the year {new_data}")
