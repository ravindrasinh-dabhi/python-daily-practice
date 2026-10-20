# Python Program to Find All Pythagorean Triplets in the Range
start=int(input("Enter the starting range : "))
end=int(input("Enter the end of the range : "))
print("This is the are the lists of all the triplets")
for i in range(start,end+1):
    for j in range(i+1,end+1):
        for k in range(j+1,end+1):
            if i**2+j**2==k**2:
                print([i,j,k])
                


