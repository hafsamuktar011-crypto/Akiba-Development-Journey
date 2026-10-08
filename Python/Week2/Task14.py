# PALINDROME CHECKER

word = input("Enter a word: ")

# Convert the word to lowercase
word = word.lower()

# Reverse the word
reversed_word = word[::-1]

if word == reversed_word:
    print("Palindrome")
else:
    print("Not a Palindrome")