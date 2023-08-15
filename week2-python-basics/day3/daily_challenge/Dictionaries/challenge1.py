word = input("input word: ")

letter_indexes = {
    letter: [index for index, char in enumerate(word) if char == letter]
    for letter in set(word)
}

print(letter_indexes)
