# Sezimgul Zhusupova Gaparova Madina,Abdunabieva Ainazik| October 27, 2026
# CSS 225 - Module 6 Team Assignment
# Number Guessing Game

import random

# Keep playing until the user chooses N.
while True:
    number = random.randint(1, 100)

    print("\n===== NUMBER GUESSING GAME =====")
    guess = int(input("Guess a number from 1 to 100: "))

    if guess == number:
        print("You guessed the correct number!")
    else:
        if guess < number:
            print("Your guess is too low. Try a higher number.")
        else:
            print("Your guess is too high. Try a lower number.")

        print("The correct number was", number)

    play = input("Would you like to guess another number (Y/N)? ").strip().upper()

    if play == "N":
        print("Thank you for playing! Goodbye!")
        break
    else:
        print("Let's play again!")