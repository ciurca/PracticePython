a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def basic():
    print(f"I'll return numbers from {a} smaller than 5.")
    print([n for n in a if n <= 5])
def extra():
    print(a)
    num = int(input("Enter a number and I'll return the list with numbers smaller than yours: "))
    print([n for n in a if n <= num])

def whichOne():
    choose = str(input("Which program do you want? Type basic or extra: "))
    if choose == "basic":
        basic()
    else:
        extra()
whichOne()

