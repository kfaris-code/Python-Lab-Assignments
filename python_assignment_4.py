1. Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

Solution:
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

Output:
Enter a number:  10
Even

2.Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.

Solution:
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

Output:
Enter your age:  20
Eligible to vote


3.Write a Python program that determines if a given year is a leap year or not.

Solution:

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


Output:
Enter a year:  2024
2024 is a leap year


4.Create a Python program that checks if a user-given number is positive, negative, or zero.

Solution:
number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

Output:
Enter a number:  30
Positive


5.Write a Python program that determines the largest of three numbers entered by the user.

Solution:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")

Output:
Enter the first number:  12
Enter the second number:  23
Enter the third number:  33
The largest number is 33.0

