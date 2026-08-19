#21 Number game

import random

def check_input(num_entered):
    if len(nums)+1 == num_entered:
        nums.append(num_entered)
    else:
        check_input(int(input("Wrong number, please enter correct num: ")))


def player_turn():
    print("Your turn")
    num_amount = int(input("How many numbers do you wish to enter? (1-3): "))
    if num_amount < 1 or num_amount > 3:
        num_amount = int(input("Please enter a valid amount (1-3): "))
    print("Enter your numbers: (press Enter after each number)")
    for i in range(num_amount):
        # num_entered = int(input())
        check_input(int(input()))

def is_game_over(nums, is_player_turn):
    if nums[-1] == 21:
        if is_player_turn:
            print("Game Over! You LOOOOOOOOOOSE")
        else:
            print("Game Over! The computer self destructed! You win!")
        return False
    else:
        return True

nums = []

print("Player 2 is Computer")
is_playing = False
is_player_turn = False

if str(input("Do you want to play the 21 number game? (Yes/No): ")).lower() == "yes":
    is_playing = True
else:
    is_playing = False

if is_playing:
    print("Enter 'F' to go first")
    if str(input("Enter 'S' to go second: ")) == "S":
        is_player_turn = False
    else:
        is_player_turn = True

while is_playing:
    if is_player_turn:
        player_turn()
        is_playing = is_game_over(nums, is_player_turn)
        if not is_playing:
            break
        is_player_turn = False
    else:
        print("Computer's turn:")
        for i in range(random.randint(1,3)):
            nums.append(nums[-1]+1) if len(nums) > 0 else nums.append(1)
            is_playing = is_game_over(nums, is_player_turn)
            if not is_playing:
                break
        print(f"Numbers after computer's turn: {nums}")
        is_player_turn = True