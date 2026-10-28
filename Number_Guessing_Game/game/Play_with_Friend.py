from .logic import check_guess
def play_with_friend():
    print("\nYou selected to play with friend")

    selector=input("\nEnter the Selector name : ")
    guesser=input("Enter the Guesser name : ")
    print("\nFirst select the Range of the number")
    starting=int(input("Enter the starting range : "))
    ending=int(input("Enter the ending range : "))

    while True : 
        try:
            secret_number=int(input(f"{selector}, select your number in range {starting} to {ending} : "))
            if starting<=secret_number<=ending:
                break
            print(f"Please, select the number in range {starting} to {ending}")
        except ValueError :
            print("Invalid input! Please enter a whole number.")


    print("\n"*50) # This will hide the number from the second player 

    print(f"\nYour Turn, {guesser}!")

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
            print(f"Congratulations {guesser}!")
            print(f"You guessed the correct number in {attempts} attempts!")
            break
        else:
            print(result)
            print(f"Attempts so far: {attempts}")