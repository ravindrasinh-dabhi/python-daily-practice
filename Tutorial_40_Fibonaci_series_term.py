#Python Program to Find the Fibonacci Series Without using Recursion
n1,n2=0,1
n=int(input("Enter the term of fibonacci series you want : "))
if n<=0:
    print("Enter the valied term")
elif n==1:
    print(f"{n} term of fibonacci series is : {n1}")
else:
    for i in range(2,n):
        sum=n1+n2
        n1=n2
        n2=sum
    print(f"{n} term of fibonacci series is : {n2}") 



