#this includes both extras
num = input("Enter a number: ")
check = input(f"Enter a number by which to divide {num}: ")
#first extra below (multiple of 4)
if int(num) % 4 == 0:
    print(f"The number ({num}) that you've entered is a multiple of 4 and is even.")
elif int(num) % 2 == 0:
    print(f"The number ({num}) that you've entered is even.")
else:
    print(f"The number ({num}) that you've entered is odd.")
#second extra
if int(num) % int(check) == 0:
    print(f"The number {num} divides evenly into {check}.")
else:
    print(f"The number {num} doesn't divide evenly into {check}.")