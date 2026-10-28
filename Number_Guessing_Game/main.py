import game.Play_with_Friend as PWF
import game.Play_with_Computer as PWC
import game.Message

game.Message.welcome_message()

game.Message.rule()

while True :
    try:
        print("\nSelect the Second Player : ")
        print("1. Computer")
        print("2. Friend")
        print("3. Exit")
        choice=int(input("Enter your choice (1,2 or 3) : "))
        if choice==1:
            PWC.play_with_computer()
            break
        elif choice==2:
            PWF.play_with_friend()
            break
        elif choice==3:
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")
    except ValueError :
        print("Invalid input! Please enter a whole number.")