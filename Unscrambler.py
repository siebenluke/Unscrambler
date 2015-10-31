import string

def printList(lst):
    """Prints out the elements in a list."""
    for element in lst:
        print(element)

def geListFromFile(filename):
    """Gets a list from the data in a given file."""
    return open(filename).read().splitlines()

def getLetterCountDict(word):
    """Gets a dictionary that maps the amount of times a letter appears in a word to a letter."""
    letterCountDict = {}
    for letter in string.ascii_lowercase:
        letterCountDict[letter] = getLetterAmount(letter, word)
    return letterCountDict

def getLetterAmount(letter, word):
    """Gets the amount of times a letter appears in a word."""
    count = 0
    for char in word:
        if letter == char:
            count += 1
    return count

def getUnscrambled(dictionary, scrambled):
    """Gets unscrambled words in a list."""
    unscrambled = []
    scrambledLetterCountDict = getLetterCountDict(scrambled)
    for word in dictionary:
        # check for length match
        if len(scrambled) == len(word):
            mismatch = False
            wordLetterCountDict = getLetterCountDict(word)
            # see if amount of letters match
            for key in scrambledLetterCountDict:
                if scrambledLetterCountDict[key] != wordLetterCountDict[key]:
                    mismatch = True
                    break
            if not mismatch:
                unscrambled.append(word)
    return unscrambled

def main():
    """Main method."""
    # keep program running until user wants to quit
    dictionary = geListFromFile('dictionary.txt')
    while True:
        scrambled = input('Please enter a scrambled English word (or "n" to quit): ').lower()
        # check if user wants to quit
        if scrambled == 'n':
            print("Exiting program")
            break
        unscrambled = getUnscrambled(dictionary, scrambled)
        # check for case where no unscrambled words are found
        if len(unscrambled) == 0:
            print("Could not find any unscrambled words for:", scrambled)
        else:
            print("Found unscrambled words for:", scrambled)
            printList(unscrambled)
        print()

if __name__ == "__main__":
    main()