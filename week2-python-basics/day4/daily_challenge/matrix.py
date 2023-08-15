matrix = [
    "7ii",
    "Tsx",
    "h%?",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!",
]

n = len(matrix)  # number of rows
m = len(matrix[0])  # number of columns

words = []
word = ""
for j in range(m):
    for i in range(n):
        if matrix[i][j].isalpha():
            word += matrix[i][j]
        else:
            if len(word) > 0:
                words.append(word)
                word = ""

print(" ".join(words))
