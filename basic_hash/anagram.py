# Given two strings, return true if they are anagrams of each other, and false if they are not. An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

# Do not use any built-in sort methods.

# Input: “silent”, “listen”
# Output: true

# Input: “frog”, “bear”
# Output: false

def anagram(string, string2):
  i = 0

  if len(string)  == len(string2):
    if string[i] in string2:
      i += 1
    else:
      return False
    return True
  else:
    return False

print(anagram("iceman", "cinema"))
    