1. Write a Python program to Count all letters, digits, and special symbols from the given string
 Input = “P@#yn26at^&i5ve”
Output: Chars = 8 Digits = 3 Symbol = 4 

Solution:
input_string = "P@#yn26at^&i5ve"
chars = sum(c.isalpha() for c in input_string)
digits = sum(c.isdigit() for c in input_string)
symbols = len(input_string) - (chars + digits)
print(f"Chars = {chars} Digits = {digits} Symbol = {symbols}")

Output:
Chars = 8 Digits = 3 Symbol = 4


2. Write a Python program to remove duplicate characters of a given string.
Input = “String and String Function” 
Output: String and Function 

Solution:
input_string = "String and String Function"
# Use a set to keep track of seen characters and build the result
result = []
seen = set()
for char in input_string:
    if char not in seen:
        seen.add(char)
        result.append(char)
output_string = "".join(result)
print(output_string)


Output:
String and Function



3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
 Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN” 
Output: UpperCase : 5 LowerCase : 18 NumberCase : 5 SpecialCase : 11 

Solution:
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase = sum(c.isupper() for c in input_string)
lowercase = sum(c.islower() for c in input_string)
numbers = sum(c.isdigit() for c in input_string)
special = len(input_string) - (uppercase + lowercase + numbers + input_string.count(' '))
print(f"UpperCase : {uppercase} LowerCase : {lowercase} NumberCase : {numbers} SpecialCase : {special}")

Output:
UpperCase : 5 LowerCase : 18 NumberCase : 5 SpecialCase : 11



4. Write a Python Count vowels in a string 
input= “Welcome to Python Assignment” 
Output: Total vowels are: 8

Solution:
input_string = "Welcome to Python Assignment"
vowels = "aeiouAEIOU"
vowel_count = sum(c in vowels for c in input_string)
print(f"Total vowels are: {vowel_count}")

Output:
Total vowels are: 8

