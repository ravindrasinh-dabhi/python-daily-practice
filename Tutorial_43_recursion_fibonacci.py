#Python Program to Find the Fibonacci Series Without using Recursion
def fibonacci_term(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_term(n-2)+fibonacci_term(n-1)

n=int(input("Enter the term of the fibonacci sequence : "))
result=fibonacci_term(n)
print(f"{n} tearm of fibonacci sequence is : {result}")
