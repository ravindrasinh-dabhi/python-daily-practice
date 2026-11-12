# This is a Python Program to find the sum of series: 1 + 1/2 + 1/3 + ….. + 1/N.
def main():
 term=int(input("Enter the number of terms: "))
 sum=0
 for i in range(1,term+1):
    s=1/i
    sum=sum+s
 print(f"The sum of the series in given term is : {sum:.2f}")

 print("Do you want to Try for other term")
 print("1.Yes")
 print("2.No")
 again=input("Enter your choice: ").upper()
 if again=="YES" or again=="1":
        main()
 else:
        print("Thank you for using the program.")

main()