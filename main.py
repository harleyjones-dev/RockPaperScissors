import random

cases = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

win = 0
draw = 0
lose = 0
while True:
    plr = input("Enter rock, paper, or scissors: ")
    bot = random.randint(1,9)
    # I have intentionally skewed the probability of a win by making the computer pick a number between 1-9

    if plr in cases.keys:
        if bot == 4 or bot == 6 or bot == 8: # These numbers are 3 random numbers I thought of in range to give a probability of a win
            print(f"{plr} beats {cases[plr]}!")
            win += 1
        elif bot == 5: # This is a random number to give a probability of a draw 
            print(f"{plr} draws {plr}")
            draw += 1
        else: # Anything that is outside the numbers above are losses
            print(f"{plr} loses to {cases[cases[plr]]}") # I indirectly find what the player will lose to
            lose += 1
    

        print(f"You have {win} wins, {draw} draws, and {lose} losses.")

        if input("Would you like to play again? (yes/no): ").lower()[0] == "n":
            break
    else:
        print("Invalid option, enter \"rock\", \"paper\" or \"scissors\"!")