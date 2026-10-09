#python program to print sand galss pattern
rows=int(input("Enter the number of rows : "))
for i in range(rows,0,-1):
    for space in range(1,rows-i+1):
        print(end=" ")
    for star in range(1,i+1):
        print("*",end=" ")
    print()
for k in range(1,rows+1):
    for space in range(1,rows-k+1):
        print(end=" ")
    for star in range(1,k+1):
        print("*",end=" ")
    print()


