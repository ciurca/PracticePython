a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(f"I'm going to print a new list that has only the even elements of this list\n{a} in in it.")
print([n for n in a if n % 2 == 0])