#
#Faris Khan
#

1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.

Solution:
def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

# Call the function
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = div(num1, num2)
print(f"The result of division is: {result}")

Output:
Enter the first number:  22
Enter the second number:  33
The result of division is: 0.6666666666666666

2. Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number 

Solution:
def square(x):
    return x ** 2

# Call the function
num = float(input("Enter a number: "))
result = square(num)
print(f"The square of {num} is: {result}")

Output:
Enter a number:  20
The square of 20.0 is: 400.0


3. Using max() and min() functions display the maximum and minimum of 5 random numbers. 

Solution:
import random

# Generate 5 random numbers
numbers = [random.randint(1, 100) for _ in range(5)]
print(f"Random numbers: {numbers}")

# Use max() and min() functions
maximum = max(numbers)
minimum = min(numbers)
print(f"The maximum number is: {maximum}")
print(f"The minimum number is: {minimum}")

Output:Random numbers: [54, 64, 14, 60, 37]
The maximum number is: 64
The minimum number is: 14


4. Accept a name from the user and display that in lower case using lower() function

Solution:
name = input("Enter your name: ")
print(f"Your name in lowercase is: {name.lower()}")

Output:
Enter your name:  FARIS
Your name in lowercase is: faris

