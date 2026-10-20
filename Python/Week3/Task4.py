# Text Statistics and Word Analyzer

# Count words.
# Count characters excluding spaces.
# Count vowels and consonants.
# Find the longest word.
# Count how many times each word appears.
# Identify repeated words

text = "Python is useful and Python is powerful."

words=text.split()
print(words)

# count word
def getcountWords(words):
    countWord=len(words)
    return countWord
print(f"the counted words are ",getcountWords(words))

# count characters
def getCharacters(text):
    characters=len(text)
    return characters
print(f"the counted characters are ",getCharacters(text))


def getVowelandConsonants(text):
    vowel = 0
    consonants = 0

    for letter in text:
        if letter.lower() in "aeiou":
            vowel += 1
        elif letter.isalpha():
            consonants += 1

    return "Number of consonants:", consonants, "Number of vowels:", vowel


print(getVowelandConsonants(text))

    
