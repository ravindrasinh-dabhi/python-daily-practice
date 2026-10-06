#Python Program to Print All Possible Combinations of Three Digits first enter the three digit number 
n=input("Enter the number ")
x=[]
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i!=j and j!=k and k!=i :
                y=n[i]+n[j]+n[k]
                x.append(y)

print("all the possible combination of the given number are : ")
for l in x:
    print(l)
                
