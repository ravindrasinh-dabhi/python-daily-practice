number=int(input("Enter the Number : "))
temp=number
factorial=1
for i in range(temp,0,-1):
    factorial=factorial*i

print(F"{number}! = {factorial}")
