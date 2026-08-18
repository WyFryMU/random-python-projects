#Word guessing game
#making this more random via RandomWords lib: https://pypi.org/project/random_word/

from random_word import RandomWords
import random

def print_chars(char_array):
    for char in char_array:
        print(char, end='')
    print()

max_guesses = 12

if int(input("Easy(0) or Hard(1): ")) == 0:
    words = ["apple","banana","orange","grape"]
    word = words[random.randint(0,len(words)-1)]
else:
    r = RandomWords()
    word = str(r.get_random_word()).lower()

word_chars = []
word_chars_final = []
guessed_chars = []
all_guessed_chars = []
for char in word:
    word_chars.append(char)
    word_chars_final.append(char)
    guessed_chars.append("_")



name = str(input("Enter your name: "))
print(f"Good luck! {name}")
print("Guess the characters")
print_chars(guessed_chars)

while max_guesses > 0:
    char_input = str(input("Guess a character: ").lower())
    if all_guessed_chars.count(char_input) == 0:
        all_guessed_chars.append(char_input)
        max_guesses -= 1
        if word_chars_final.count(char_input) > 0:
            for i in range(word_chars.count(char_input)):
                guessed_chars[word_chars.index(char_input)] = char_input
                word_chars[guessed_chars.index(char_input)] = "_"
            print_chars(guessed_chars)
        else:
            print(f"Wrong, you have {max_guesses} more guesses")
            print_chars(guessed_chars)

        if (guessed_chars == word_chars_final):
            print(f"You win! The word is: {word}")
            break
    else:
        char_input = str(input("Already guessed, try another character: ").lower())

if max_guesses == 0:
    print(f"You lost! The word is: {word}")