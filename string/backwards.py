# Description
# Given a string of words, write a function that returns a new string that contains the words in reverse order.

# Input: “popcorn is so cool isn’t it yeah i thought so”
# Output: “so thought i yeah it isn’t cool so is popcorn”

def backwards(string):
    words = string.split()
    reversed= " ".join(words[::-1])
    return reversed

print(backwards("popcorn is so cool isn’t it yeah i thought so"))