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
def getCountWords(words):
    countWord=len(words)
    return countWord
print(f"the counted words are ",getCountWords(words))

# count characters
def countCharacters(text):
    characters=len(text)
    return characters
print(f"the counted characters are ",countCharacters(text))


def countVowelandConsonants(text):
    vowel = 0
    consonants = 0

    for letter in text:
        if letter.lower() in "aeiou":
            vowel += 1
            # to avoid space,punctuation
        elif letter.isalpha():          
            consonants += 1

    return "Number of consonants:", consonants, "Number of vowels:", vowel
print(countVowelandConsonants(text))


def getLongestWord(words):
    if len(words) == 0:
        return "no word"

    longest = words[0]
    index = 1

    while index < len(words):
        if len(words[index]) > len(longest):
            longest = words[index]

        index += 1

    return longest

print("The longest word is:", getLongestWord(words))


def getLongestWord(words):
    if len(words) == 0:
        return "No words"

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

print("The longest word in the text is:", getLongestWord(words))
               
