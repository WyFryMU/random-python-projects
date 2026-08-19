#Rock paper scissors

import random

choices = ["Rock","Paper","Scissors"]

def intro():
    print("Winning rules of RPS are:")
    print("Rock vs Paper -> Paper wins")
    print("Rock vs Scissors -> Rock wins")
    print("Paper vs Scissors -> Scissors wins")

def computer_choice(): #I guess this is overkill but meh
    return random.randint(1,3)

def validate_choice(choice):
    if choice > 3 or choice < 1:
        return validate_choice(int(input("Enter a VALID choice: \n 1 - Rock \n 2 - Paper \n 3 - Scissors\n > ")))
    else:
        return choice

def player_turn():
    return validate_choice(int(input("Enter your choice: \n 1 - Rock \n 2 - Paper \n 3 - Scissors\n > ")))

def combat(player_choice, comp_choice):
    print(f"User choice is: {choices[player_choice-1]}")
    print(f"Computer choice is: {choices[comp_choice-1]}")
    if player_choice == comp_choice:
        print("<== Draw ==>")
    else:
        if player_choice == 2 and comp_choice == 1: #Paper vs Rock
            print("<== User wins! ==>")
        if player_choice == 3 and comp_choice == 2: #Scissors vs Paper
            print("<== User wins! ==>")
        if player_choice == 1 and comp_choice == 3: #Rock vs Scissors
            print("<== User wins! ==>")
        else:
            print("<== User loses! ==>")
    return True if str(input("Do you want to play again? (Y/N): ")) == "Y" else False

def main():
    is_playing = True
    intro()
    while is_playing:
        is_playing = combat(player_turn(), computer_choice())
    print("Thanks for playing!")

if __name__ == '__main__':
    main()