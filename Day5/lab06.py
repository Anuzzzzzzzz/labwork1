"""
 . Write a Python program that accepts a word from the user and reverse it
"""
words = input("Enter a words to reverse: ")

for char in range(len(words) - 1, -1, -1):
    print(words[char], end="")