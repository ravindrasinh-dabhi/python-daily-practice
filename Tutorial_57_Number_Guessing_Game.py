# Number Guessing Game 
# This is a simple number guessing game where the player has to guess a randomly generated number within a certain range.
# The player will receive feedback on whether their guess is too high, too low, or correct.
import random 
number=random.randint(0, 5001)  # Generate a random number between 1 and 5000
while True:
    choice=int(input("Enter Your choice : "))
    if choice==number:
        print("You guessed it right! The number was", number)
        break
    elif choice>number:
        print("Your guess is too high. Try again.")
    else:
        print("Your guess is too low. Try again.")
