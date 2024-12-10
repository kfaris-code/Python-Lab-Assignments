#
#Faris Khan
#

Q.1 Check Even or Odd Using input() and Ternary Operators

Solution:
# Input from user
number = int(input("Enter a number: "))
# Ternary operator to check even or odd
result = "Even" if number % 2 == 0 else "Odd"
print(f"The number {number} is {result}.")

Output:
Enter a number:  20
The number 20 is Even.

Q.2 Using input function take two number and then swap the number 

Solution:
# Input from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Swapping using a temporary variable
print(f"Before swapping: num1 = {num1}, num2 = {num2}")
num1, num2 = num2, num1
print(f"After swapping: num1 = {num1}, num2 = {num2}")

Output:
Enter the first number:  10
Enter the second number:  20
Before swapping: num1 = 10, num2 = 20
After swapping: num1 = 20, num2 = 10


Q.3 Write a Program to Convert Kilometers to Miles 

Solution: 
# Input kilometers from user
kilometers = float(input("Enter the distance in kilometers: "))
# Conversion factor
conversion_factor = 0.621371
# Conversion
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")

Output:
Enter the distance in kilometers:  30
30.0 kilometers is equal to 18.64 miles.

Q.4  Find the Simple Interest on Rs. 200 for 5 years at 5% per year. write the programme in python for these question

Solution:
# Principal, rate, and time
principal = 200
rate = 5
time = 5
# Simple Interest formula
simple_interest = (principal * rate * time) / 100
print(f"The Simple Interest on Rs. {principal} for {time} years at {rate}% is Rs. {simple_interest}.")

Output:
The Simple Interest on Rs. 200 for 5 years at 5% is Rs. 50.0.
