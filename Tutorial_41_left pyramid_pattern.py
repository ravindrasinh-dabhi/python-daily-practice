#pyhton program to print lft side right angle pattern
column=int(input("Enter the column : "))
for i in range(1,column+1):
    for space in range(1,column-i+1):
        print(" ",end=" ")

    for star in range(1,i+1):
        print("*",end=" ")
    print()

for k in range(column-1,0,-1):
    for space in range(1,column-k+1):
        print(" ",end=" ")
    for star in range(1,k+1):
        print("*",end=" ")
    print()
