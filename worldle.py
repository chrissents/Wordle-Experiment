import random

possible_words = ["green", "water", "light", "quake", "magma"]



word = random.choice(possible_words)

# color for printing
default = '\033[0m'
green = '\033[92m'
yellow = '\033[33m'

# generates hint with correct answer
def generate_hint(user_guess):
    color = default
    hint = ""
    for i in range(5):
        if (user_guess[i] == word[i]):
            color = green
        elif (user_guess[i] in word):
            color = yellow
        else:
            color = default

        hint = color + user_guess + default

        return hint


def game_loop():
    guess = ""
    for i in range(6):
        guess = input("What is your guess?: ")
        print(generate_hint(guess))
        if (guess == word):
            print("Congratulations! You got the word correct.")
            break

game_loop()