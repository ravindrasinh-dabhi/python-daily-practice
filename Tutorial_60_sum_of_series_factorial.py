# This is a Python Program to find the sum of series:1+1/1!+1/2!+1/3!+…1/N!.
import math

from Personal_Expense_Tracker import main
def sum_of_series_factorial():
 term=int(input("Enter the number of terms: "))
 sum=1
 for i in range(1,term+1):
    sum=sum+(1/math.factorial(i))


 print(f"The sum of series is: {sum:.2f}")

 print("Do you want to Try for other term")
 print("1.Yes")
 print("2.No")
 again=input("Enter your choice: ").upper()
 if again=="YES" or again=="1":
        sum_of_series_factorial()
 else:
        print("Thank you for using the program.")

sum_of_series_factorial()