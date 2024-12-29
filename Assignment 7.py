1. Write a Python program to count the occurrences of each word in a

Solution :
string = "To change the overall look of your document. To change the look available in the gallery"
# Convert to lowercase and split into words
words = string.lower().split()
# Create a dictionary to store word counts
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

Output:
{'to': 2, 'change': 2, 'the': 3, 'overall': 1, 'look': 2, 'of': 1, 'your': 1, 'document.': 1, 'available': 1, 'in': 1, 'gallery': 1}

2. Write a Python program to remove a newline in Python

String = "\nBest \nDeeptech \nPython \nTraining\n"

Solution:
string = "\nBest \nDeeptech \nPython \nTraining\n"
# Remove newlines
cleaned_string = string.replace("\n", "")
print(cleaned_string)

Output:
Best Deeptech Python Training


3. Write a Python program to reverse words in a string

String = “Deeptech Python Training”

Solution:
string = "Deeptech Python Training"
# Split the string into words, reverse them, and join back
reversed_string = " ".join(string.split()[::-1])
print(reversed_string)

Output:
Training Python Deeptech


4. Write a Python program to count and display the vowels of a given text

String=”Welcome to python Training”

Solution:
string = "Welcome to python Training"
# Define vowels
vowels = "aeiouAEIOU"
# Count vowels
vowel_count = sum(1 for char in string if char in vowels)
# Display vowels
found_vowels = [char for char in string if char in vowels]
print(f"Number of vowels: {vowel_count}")
print(f"Vowels: {', '.join(found_vowels)}")

Output:
Number of vowels: 9
Vowels: e, o, e, o, o, a, i, i, a

