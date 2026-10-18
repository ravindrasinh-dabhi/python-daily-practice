import math as m 
print("Equation form : ax^2+bx+c")
a=int(input("Enter the Cofficent of x^2 : "))
b=int(input("Enter the Cofficent of x : "))
c=int(input("Enter the constant : "))


if b*b < 4*a*c:
    print("Roots are Complex")
elif b*b==4*a*c:
    d=m.sqrt(b**2-4*a*c)
    x1=(-b +d)/2*a
    print("Roots are real and Equal ")
    print(f"x1,x2={x1}")
else :
    d=m.sqrt(b**2-4*a*c) 
    x1=(-b +d)/2*a
    x2=(-b - d)/2*a
    print("Roots are real and distinct")
    print(f"x1={x1},x2={x2}")







