import datetime
name = input("Enter your name: ")
age = int(input(f"{name}, enter your age: "))
onehundred = datetime.datetime.now().year - age + 100
message = (f"{name}, you will be 100 in {onehundred}.")
print(message)
num = int(input("Enter how many times do you want to print the previous message: "))
print((f"{message}\n")*num)
