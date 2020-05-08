while True:
    rps1 = input("Player 1, what do you choose? You can choose between rock, paper and scissors: ")
    rps2 = input("Player 2, what do you choose? You can choose between rock, paper and scissors: ")
    if rps1 == "rock" and rps2 == "scissors" or rps1 == "scissors" and rps2 == "paper" or rps1 == "paper" and rps2 == "rock":
        still = input("Player one wins! If you want to quit, enter quit, otherwise, enter continue: ")
        if still == "quit":
            break
        else:
            continue
    elif rps2 == "rock" and rps1 == "scissors" or rps2 == "scissors" and rps1 == "paper" or rps2 == "paper" and rps1 == "rock":
        still = input("Player two wins! If you want to quit, enter quit, otherwise, enter continue: ")
        if still == "quit":
            break
        else:
            continue
    else:
        still = input("It's a tie! If you want to quit, enter quit, otherwise, enter continue: ")
        if still == "quit":
            break
        else:
            continue