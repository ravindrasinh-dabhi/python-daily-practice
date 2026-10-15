# Python Program to Convert Gray to Binary Code
print("Only Enter Gray code if you enter decimal number of any other number you will get the wrong answer")
s=input("Enter the Gray code : ")


b = s[0]

for i in range(1, len(s)):
    b += str(int(b[i-1]) ^ int(s[i]))

print("Binary code:", b)

# Here we have to use resultant bit of the xor so we are using modifing of b 
c=0
Binary=[]
for i in range(len(s)):
    if i==0:
        c=s[0]
        Binary.append(s[0])
    else:
        c=int(c)^int(s[i])
        Binary.append(str(c))


Binary_code="".join(Binary)
print(f"Binary code of {s} is {Binary_code}")

        

