# Given a string, find the most commonly occurring letter.

# Input: “peter piper picked a peck of pickled peppers”
# Output: “p”


def basic(string):
    i = 0
    letters = {}
    mostCount = 0
    mostLetters = 0

    while i < len(string):
        if letters.get(string[i]):
            letters[string[i]] += 1
        else:
            letters[string[i]] = 1

        if letters[string[i]] > mostCount:
            mostCount = letters[string[i]]
            mostLetters = string[i]
        i += 1

    return mostLetters

print(basic("peter piper picked a peck of pickled peppers"))


