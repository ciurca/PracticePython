import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def basic():
    print(f"I'm going to print a list that contains only the elements that are common between \n{a} and \n{b}.\n")
    print([n for n in a if n == n in b])
def extra():
    c = random.sample(range(1, 100), 11)
    d = random.sample(range(1, 100), 13)
    print(f"I'm going to print a list that contains only the elements that are common between \n{c} and \n{d}.\n")
    listnum = [n for n in c if n == n in d]
    if not listnum:
        print("No common elements. :(")
    else:
        print(f"Here are the number(s): {listnum}")
def whichOne():
    choose = str(input("Which program do you want? Type basic or extra: "))
    if choose == "basic":
        basic()
    else:
        extra()
whichOne()