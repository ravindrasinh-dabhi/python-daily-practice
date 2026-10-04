#Python Program to Find Whether a Number is a Power of Two
n=int(input("Enter the number : "))
temp=str(bin(n))
zeros=(temp.count("0")-1)
if n&(n-1)==0:
    print("{} is power of two ".format(n))
    print(f"{n} is {zeros} power of 2 ")
    print(n," = ",2,"^",zeros)
else:   
    print(f"{n} is not power of two ")

