# Python Program to Print Pascal Triangle
from math import factorial
rows=int(input("Enter the Number of rows : "))
for i in range(rows):
    for space in range(1,rows-i):
      print(end=" ")
    for star in range(i+1):
      
      n=factorial(i)//(factorial(star)*factorial(i-star))
      print(n,end=" ")
    print("")