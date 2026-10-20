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
def getcountWords(words):
    countWord=len(words)
    return countWord
print(f"the counted words are ",getcountWords(words))


def getCharacters(text):
    characters=len(text)
    return characters
print(f"the counted characters are ",getCharacters(text))

