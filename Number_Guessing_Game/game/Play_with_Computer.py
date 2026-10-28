import random
from .logic import check_guess
def play_with_computer():
    print("\nYou selected to play with computer")

    print("\nFirst select the Range of the number")
    starting=int(input("Enter the starting range : "))
    ending=int(input("Enter the ending range : "))

    secret_number=random.randint(starting,ending)

    print(f"\nYour Turn!")

    print(f"Guess the number in range {starting} to {ending}")

    attempts=0

    while True :
        try:
            guess=int(input("Enter your guess : "))

            if not starting<=guess<=ending:
                print(f"Please, select the number in range {starting} to {ending}")
                continue
        except ValueError :
            print("Invalid input! Please enter a whole number.")
            continue

        attempts+=1
        result=check_guess(guess,secret_number)
        if result=="Congratulations! You've guessed the correct number!":
            print(f"Congratulations!")
            print(f"You guessed the correct number in {attempts} attempts!")
            break
        else:
            print(result)
            print(f"Attempts so far: {attempts}")