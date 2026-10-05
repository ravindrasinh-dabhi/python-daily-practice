#Python Program to Find All Perfect Squares in the Given Range
import math
n1=int(input("Enter the starting range : "))
n2=int(input("Enter the ending range : "))
perfect_isqrt=[]
for i in range(n1,n2+1):
    root=math.isqrt(i)
    if root*root==i:
        perfect_isqrt.append(i)

print("Perfect squre in given range : ")
for j in perfect_isqrt:
    print(j,end=" ")
        
