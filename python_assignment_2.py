#
#Faris Khan
#


Q.1 Write a program for arithmatic operators
Solution:
# Arithmetic Operators
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

Output:
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
Modulus: 0
Exponentiation: 100000
Floor Division: 2

Q.2 Write a program for assignment operators
Solution:# Assignment Operators
x = 10
print("Initial value:", x)

x += 5  # x = x + 5
print("After += 5:", x)

x -= 3  # x = x - 3
print("After -= 3:", x)

x *= 2  # x = x * 2
print("After *= 2:", x)

x /= 2  # x = x / 2
print("After /= 2:", x)

x %= 3  # x = x % 3
print("After %= 3:", x)

Output:
Initial value: 10
After += 5: 15
After -= 3: 12
After *= 2: 24
After /= 2: 12.0
After %= 3: 0.0



Q.3Write a program for Bitwise operators 
Solution:
# Bitwise Operators
a = 6  # 110 in binary
b = 3  # 011 in binary

print("Bitwise AND:", a & b)  # 010 (2)
print("Bitwise OR:", a | b)   # 111 (7)
print("Bitwise XOR:", a ^ b)  # 101 (5)
print("Bitwise NOT of a:", ~a)  # -(a+1)
print("Left Shift (a << 1):", a << 1)  # 1100 (12)
print("Right Shift (a >> 1):", a >> 1)  # 011 (3)

Output:
Bitwise AND: 2
Bitwise OR: 7
Bitwise XOR: 5
Bitwise NOT of a: -7
Left Shift (a << 1): 12
Right Shift (a >> 1): 3


Q.4 Write a program to calculate greatest of three numbers.
Solution:
# Greatest of Three Numbers
a = 15
b = 25
c = 20

if a > b and a > c:
    print("Greatest:", a)
elif b > c:
    print("Greatest:", b)
else:
    print("Greatest:", c)

Output:
Greatest: 25




1.      Calculate the area of a circle.
Solution:
# Area of a Circle
import math

radius = 7
area_circle = math.pi * radius ** 2
print("Area of the Circle:", area_circle)

Output:
Area of the Circle: 153.93804002589985


2.      Calculate the area of a triangle.
Solution:
# Area of a Triangle
base = 10
height = 5
area_triangle = 0.5 * base * height
print("Area of the Triangle:", area_triangle)

Output:
Area of the Triangle: 25.0


3.      Calculate the area of a rectangle.
Solution:
# Area of a Rectangle
length = 8
width = 4
area_rectangle = length * width
print("Area of the Rectangle:", area_rectangle)

Output:
Area of the Rectangle: 32


4.      Calculate the area of a square
Solution:
# Area of a Square
side = 6
area_square = side ** 2
print("Area of the Square:", area_square)

Output:
Area of the Square: 36
