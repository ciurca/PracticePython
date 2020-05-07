#warning: it's character sensitive
word = str(input("Check if a word is a palindrome or not: "))
if word[::-1] == word:
    print(f"You word {word} is a palindrome.")
else:
    print(f"You word {word} isn't a palindrome.")