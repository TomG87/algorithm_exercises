# Given a string, write a function that returns the first occurence of two duplicate characters in a row, and return the duplicated character.

# Input: “abcdefghhijkkloooop”
# Output: “h”

def duplicate(string):
    i = 0
    i2 = 1

    while i < len(string):
        if string[i] == string[i2]:
            return string[i]
        else:
            i += 1
            i2 += 1

print(duplicate("abcdefghhijkkloooop"))