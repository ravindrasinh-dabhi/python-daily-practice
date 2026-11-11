#Python Program to Print an Identity Matrix
def main():
 n=int(input("Enter the size of the identity matrix: "))
 for i in range(n):
    for j in range(n):
        if i==j:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
 print("Identity Matrix of size", n, "is printed above.")
 print("Do you want to print other size identity matrix")
 print("1.Yes")
 print("2.No")
 again=input("Enter your choice: ").upper()
 if again=="YES" or again=="1":
        main()
 else:
        print("Thank you for using the program.")

main()