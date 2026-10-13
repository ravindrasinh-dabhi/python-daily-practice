#This is a Python program to convert binary to Gray code.
n=input("Enter the Binary number ")
temp=n
temp1=str(n)
gray=[]
for i in range(len(temp1)):
    if i==0:
        gray.append(str(temp1[i]))
    elif i==1:
        second=int(temp1[0])^int(temp1[1])
        gray.append(str(second))
    else:
        if i<len(temp1):

          x=int(temp1[i])^int(temp[i-1])
          gray.append(str(x))

gray_code="".join(gray)
print(f"The gray code of {n} is {gray_code}")

# there is also another way like using function but it is hard to undersatnd for begineer which right now i am 

def binary_to_gray(n):
    """Convert Binary to Gray codeword and return it."""
    n = int(n, 2) # convert to int
    n ^= (n >> 1)
 
    # bin(n) returns n's binary representation with a '0b' prefixed
    # the slice operation is to remove the prefix
    return bin(n)[2:]
 
 
g = input('Enter binary number: ')
b = binary_to_gray(g)
print('Gray codeword:', b)