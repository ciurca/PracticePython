import datetime
name = input("Hello. Enter your name: ")
age = input(f"{name}, enter your age: ")
year = datetime.datetime.now().year - int(age) + 100
print(f"{name}, you'll be 100 in the year {year}")
#bonus below
num1 = int(input("Give me another number: "))
print((f"\n{name}, you'll be 100 in the year {year}") * num1)