# Project Module 2: Guessing Game

# Develop a number guessing game where the program randomly selects a number.
# Use loops and conditional statements to provide feedback and control the game flow.

# Example Code:

import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break

guessing_game()
