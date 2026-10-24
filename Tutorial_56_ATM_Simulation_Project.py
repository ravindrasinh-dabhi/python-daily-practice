# ATM Simulation Project
correct_pin="4567"
balance=5000
print("\n=======================")
print("     Welcome to ATM")
print("=======================")
pin=input("Enter the Pin : ")
if pin==correct_pin:
    while True :
        print("------ATM Menu------")
        print("1. Cheack Balance")
        print("2. Withdraw Money")
        print("3. Deposite Money")
        print("4. Exit")

        choice=input("\nEnter Your Choice : ")
        if choice=="1":
            print(f"available balance : {balance}")
        elif choice=="2":
            amount=int(input("\nEnter the amount to withdraw : "))
            if amount<=0:
                print("Invalid amount. amount should be greter then zero")
            elif amount>balance:
                print("Insufficient balance")
            else:
                balance=balance-amount
                print(f"withdrawal of amount Rs. {amount} successful")
                print(f"Remaining balance : Rs. {balance}")
        elif choice=="3":
            amount=int(input("\nEnter The amount to Deposite : "))
            if amount<=0:
                print("Invalid amount. amount should be greter then zero")
            else:
                balance=balance+amount
                print(f"Deposite of amount Rs. {amount} successful")
                print(f"Available balance : Rs. {balance}")
        elif choice=="4":
            print("THANK YOU FOR COMING")
            print("HAVE A NICE DAY")
            break
else:
    print("invalid pin. Please enter the correct pin")


