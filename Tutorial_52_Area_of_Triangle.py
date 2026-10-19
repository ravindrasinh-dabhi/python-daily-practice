# Python Program to Find the Area of a Triangle
import math as m
def area_of_triangle(a,b,c):
    s=(a+b+c)/2
    return m.sqrt(s*(s-a)*(s-b)*(s-c))
print("Before entering the lenght make sure all are in the same units")
print("If it is not in the same unit than make in the same unit and than enter the value")
print("for proper result")
a=int(input("Enter the lenght of first side : "))
b=int(input("Enter the lenght of second side : "))
c=int(input("Enter the lenght of third side : "))
type_of_tri=""
if a==b!=c or b==c!=a or c==a!=b:
    type_of_tri="Isosceles triangle"
    print("This is Isosceles triangle")
    print("In this triangle Two sides are equal, so the angles opposite those sides are also equal.")
elif a==b==c:
    type_of_tri="Equilateral triangle"
    print("This is Equilateral triangle")
    print("All three sides are equal, so all three angles are 60degree.")
else:
    type_of_tri="Scalene triangle"
    print("This is Scalene triangle")
    print("All three sides and all three angles are different.")
area=area_of_triangle(a,b,c)
print(f"Are of the given {type_of_tri} is {area:.3f} unit ")
print("Unit is going to be the same as you enter in the input but this is area")


