import random

cases = {"rock": "scissors","paper": "rock","scissors": "paper"}
win, draw, lose = 0, 0, 0

while True:
    plr = input("Enter rock, paper, or scissors: ")
    bot = random.choice(list(cases.keys()))

    if plr in cases:
        if plr[1] != bot:
            print(f"{plr.title()} beats {bot}!")
            win += 1
        elif plr == bot:
            print(f"{plr.title()} draws {bot}.")
            draw += 1
        else:
            print(f"{plr.title()} loses to {bot}.")
            lose += 1
    
        print(f"You have {win} wins, {draw} draws, and {lose} losses.")

        if input("Would you like to play again? (yes/no): ").lower()[0] == "n":
            break
    else:
        print("Invalid option, enter \"rock\", \"paper\" or \"scissors\"!")