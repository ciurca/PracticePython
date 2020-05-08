import random
guesses = 0
right = 0
print("We'll play a guessing game! If you want to stop, just type in exit!")
while True:
    num = random.randint(1,9)
    guess = input("Guess the number, betweeen 1 and 9: ")
    if guess == "exit":
        print(f"You have taken {guesses} guesses and you've got {right} right!")
        break
    elif int(guess) == num:
        print("You guessed it!")
        right += 1
    elif int(guess) > num:
        print("Too high!")
        guesses += 1
    else:
        print("Too low!")
        guesses += 1