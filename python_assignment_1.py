#
#Faris Khan
#

Q.1 Print Helloworld

Solution:
print("hello world")

Output:
hello world


Q.2 Describe Local Variable And Global Variable Code

Solution:
A local variable is defined inside a function and can only be accessed within that function.
 A global variable is defined outside any function and can be accessed by any function within the same program.

#Global variable
a = 20
def fun():
    #local variable
    b = 10
    print("inside function - local variable a:",a)
    print("inside function - global variable b:",b)

fun()
print("outside function - global variable a:",a)

Output:
inside function - local variable a: 20
inside function - global variable b: 10
outside function - global variable a: 20

Q.3: Write A Code That Describe Indentation Error

Solution:
def function():
    print("Hello, World!")
    print("This is properly indented.")
  print("This line will cause an IndentationError.")

function()

Output:
 File <string>:5
    print("This line will cause an IndentationError.")
                                                      ^
IndentationError: unindent does not match any outer indentation level

Q.4: Write A Code That Describe Local and Global Variable with Same Name

Solution:
a = 10  # Global Variable

def example_function():
    a = 5  # Local Variable
    print("Inside function - Local Variable x:", x)

example_function()
print("Outside function - Global Variable x:", x)

Output:
Inside function - Local Variable a: 5
Outside function - Global Variable a: 10



Q.5: Write A Code For String, Int and Float Input

Solution:

string_input = input("Enter a string: ")


int_input = int(input("Enter an integer: "))


float_input = float(input("Enter a float: "))


print("You entered the string:", string_input)
print("You entered the integer:", int_input)
print("You entered the float:", float_input)

Output:
Enter a string: Hello
Enter an integer: 42
Enter a float: 3.14


You entered the string: Hello
You entered the integer: 42
You entered the float: 3.14


