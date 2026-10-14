
s = input("Enter the Binary number: ")

def binary_to_gray(i):
    # Base case
    if i == 0:
        return s[0]

    # Recursive case
    previous = binary_to_gray(i - 1)

    bit = int(s[i - 1]) ^ int(s[i])

    return previous + str(bit)

result = binary_to_gray(len(s) - 1)
print(f"the gray code of {s} is {result}")
