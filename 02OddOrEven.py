def yesNo():
    while True:
        try:
            yesorno = str(input("Do you want to try another program? Enter yes or no: "))
            if yesorno == "yes":
                whichOne()
            else:
                break
        except ValueError:
            print("You need to enter yes or no.")
def basic():
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("You need to enter a number.")
    if num % 2 == 0:
        print(f"The number {num} is even.")
    else:
        print(f"The number {num} isn't even.")
    yesNo()

def bonus1():
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("You need to enter a number.")
    if num % 2 == 0 and num % 4 == 0:
        print(f"The number {num} is even and is a multiple of 4.")
    elif num % 2 == 0:
        print(f"The number {num} is even.")
    else:
        print(f"The number {num} isn't even.")
    yesNo()
def bonus2():
    while True:
        try:
            num3 = int(input("Enter a number to check: "))
            break
        except ValueError:
            print("You need to enter a number")
    while True:
        try:
            check = int(input("Enter a number to divide by: "))
            break
        except ValueError:
            print("You need to enter a number")
    if check % num3 == 0:
        print(f"The number {check} divides evenly into {num3}.")
    else:
        print(f"The number {check} doesn't divide evenly into {num3}.")
    yesNo()

class IncorrectProgram(Exception):
   pass

def whichOne():
    while True:
        try:
            program = input("Which program do you want to check out? basic/bonus1/bonus2: ")
            if program == "basic":
                basic()
            elif program == "bonus1":
                bonus1()
            elif program == "bonus2":
                bonus2()
            else:
                raise IncorrectProgram
            break
        except IncorrectProgram:
            print("You need to enter basic, bonus1 or bonus2.")
whichOne()