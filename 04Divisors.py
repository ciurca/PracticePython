num = int(input("Enter a number and I'll return all the divisors of that number: "))
x = range(1, num + 1)
print([n for n in x if num % n == 0])