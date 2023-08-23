# Given a string, write a function that returns true if it is a palindrome, and false if it is not. (A palindrome is a word that reads the same both forward and backward.)

# Input: “racecar”
# Output: true

# Input: “baloney”
# Output: false

def palindrome(string):
    if string == string[::-1]:
        return True 
    else:
        return False
    
print(palindrome("racecar"))