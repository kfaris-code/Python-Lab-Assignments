#
#Faris Khan
#

1. Write a python program to reverse a number using a while loop. 

Solution
# Program to reverse a number
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

# Input from user
number = int(input("Enter a number to reverse: "))
print("Reversed Number:", reverse_number(number))

Output
Enter a number to reverse:  20
Reversed Number: 2


2. Write a python program to check whether a number is palindrome or not?

Solution
 # Program to check whether a number is palindrome
def is_palindrome(num):
    original_num = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return original_num == reversed_num

# Input from user
number = int(input("Enter a number to check if it is a palindrome: "))
if is_palindrome(number):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

Output:
Enter a number to check if it is a palindrome:  31
The number is not a palindrome.


3. Write a python program finding the factorial of a given number using a while loop. 

Solution
# Program to find the factorial of a number
def factorial(num):
    result = 1
    while num > 1:
        result *= num
        num -= 1
    return result

# Input from user
number = int(input("Enter a number to find its factorial: "))
print("Factorial:", factorial(number))

Output
Enter a number to find its factorial:  20
Factorial: 2432902008176640000


4. Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.

Solution
# Program to sum numbers until 0 is entered
def sum_until_zero():
    total = 0
    while True:
        num = int(input("Enter a number (0 to stop): "))
        if num == 0:
            break
        total += num
    return total

# Display the sum
print("Total Sum:", sum_until_zero())


Output
Enter a number (0 to stop):  10
Enter a number (0 to stop):  20
Enter a number (0 to stop):  30
Enter a number (0 to stop):  0
Total Sum: 60


5. Program to check whether the given number is Armstrong or not.
Solution 
# Program to check whether a number is Armstrong or not
def is_armstrong(num):
    order = len(str(num))
    sum_of_powers = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** order
        temp //= 10
    return num == sum_of_powers

# Input from user
number = int(input("Enter a number to check if it is an Armstrong number: "))
if is_armstrong(number):
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")

Output
Enter a number to check if it is an Armstrong number:  110
The number is not an Armstrong number.

