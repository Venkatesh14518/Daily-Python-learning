# write a short command line game

# 1. ask the user for their name: (use the input() function)

# Say hello to them with their name
# If their name begins with a vowel say something funny about that ("Aha! Oho! Uhu! Ihi! etc", your name begins with a vowel!)
# If their name begins with a consonant make an even better joke about it.

# Ask them to pick a number between 1 and 10.
# If they guessed the right number, tell them they won
# Else, tell them they lost.

import random  # import the random module so we can generate random numbers

random_number = random.randint(1, 10)   # randint(1, 10) picks a random number between 1 and 10 *inclusive*

name = input("What is your name? ")     # ask for user's name

first_letter = name[0].lower()          # take the first letter of the name, convert to lowercase to simplify checks

# greet the user
if first_letter in "aeiou":             # check if first letter is a vowel
    print(f"Hello {name}! Aha! Your name begins with a vowel!")  
else:
    print(f"Hello {name}! Oho! A strong consonant start — very powerful name!")  

# ask the user to guess a number
guess = input("Pick a number between 1 and 10: ")   # input() returns a string
guess = int(guess)                                  # convert guess to integer so we can compare

# compare the guess with the random number
if guess == random_number:                          # user guessed correctly
    print("Wow! You won! 🎉")
else:
    print("Oops! You lost! 😄 Better luck next time!")
    print(f"The correct number was {random_number}")  # optional reveal
