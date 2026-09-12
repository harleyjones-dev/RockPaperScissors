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

    if plr == "rock" or plr == "scissors" or plr == "scissors":
        if bot == 4 or bot == 6 or bot == 8:
            print(f"{plr} beats {cases[plr]}!")
            win += 1
        elif bot == 5:
            print(f"{plr} draws {plr}")
            draw += 1
        else:
            print(f"{plr} loses to {cases[cases[plr]]}")
            lose += 1
    

        print(f"You have {win} wins, {draw} draws, and {lose} losses.")

        if input("Would you like to play again? (yes/no): ").lower()[0] == "n":
            break
    else:
        print("Invalid option, enter \"rock\", \"paper\" or \"scissors\"!")