#Python Program to Find the Factorial of a Number Without Recursion
def fact():
    n=int(input("Enter the number : "))
    def factorial(n):
        if n==0 or n==1:
            return 1
        else :
            return n*factorial(n-1)
    factorial_n=factorial(n)
    print(f"{n}! = {factorial_n}")
    print("Do you want to try again")
    print("1.Yes")
    print("2.No")
    again=input("Enter you are choise : ").upper()
    if again=="1" or again=="YES":
        fact()
    else:
        print("Thank you for using")



fact()
    

