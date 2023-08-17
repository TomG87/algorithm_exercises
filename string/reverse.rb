# VIDEO: Algorithm Ladder #02: Basic String

# Write a function that returns the reverse of a given string.

# Input: “abcde”
# Output: “edcba”

def backwards(string) 
  return string.split("").reverse.join("")
end

p backwards("abcde")


