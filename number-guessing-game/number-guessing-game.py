#Number guessing game
import random

lower_range = int(input("Enter lower range: "))
upper_range = int(input("Enter upper range: "))

correct_number = random.randint(lower_range, upper_range)
num_curr_guesses = 0
num_max_guesses = 7 #Can put whatever

while num_max_guesses > num_curr_guesses:
    num_curr_guesses += 1
    num_input = int(input("Guess the number: "))
    if num_input == correct_number:
        print(f"Guess {num_curr_guesses}: {num_input} -> Correct!")
        break
    else:
        print(f"Guess {num_curr_guesses}: {num_input} -> {"Too low" if num_input < correct_number else "Too high"}")
        if num_curr_guesses == num_max_guesses:
            print(f"Game Over! Random number -> {correct_number} -> Correct!")