#Python Program to Find Product of Two Numbers using Recursion
def product(a,b):
    if b == 0:
        return 0
    return a+product(a,b-1)
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))

print(f"product is : {product(a,b)}")
