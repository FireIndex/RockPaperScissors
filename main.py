import os
import random
import graphic

def play():
    graphic_logo = [graphic.rock, graphic.paper, graphic.scissors]

    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

    computer_choice = random.randint(0, 2)

    if user_choice >= 0 and user_choice <= 2:
        print(f"Your choice {graphic_logo[user_choice]}")
        print(f"Computer choice {graphic_logo[computer_choice]}")

        if user_choice == computer_choice:
            print("Match Drow")
        elif user_choice == 0 and computer_choice == 2:
            print("You win.")
        elif user_choice == 1 and computer_choice == 0:
            print("You win.")
        elif user_choice == 2 and computer_choice == 1:
            print("You win.")
        else:
            print("You lose")

        def clear():
            os.system('cls')

        if input("Do you want to play a game of 'Rock Paper Secissor'? Type 'y' or 'n': ").lower() == 'y':
            clear()
            play()

play()