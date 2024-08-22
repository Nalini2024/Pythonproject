'''Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.'''

Side1 = int(input("Enter side1 value "))
Side2 = int(input("Enter side2 value "))
Side3 = int(input("Enter side3 value "))

if Side1 == Side2 == Side3:
    print(f"Sides {Side1,Side2,Side3} is  an Equilateral Triangle")

elif (Side1 == Side2) or (Side2 == Side3) or (Side1 == Side3):
    print(f"Sides {Side1, Side2, Side3} is  an Isosceles Triangle")

else:
    print(f"Sides {Side1, Side2, Side3} is  a Scalene Triangle")