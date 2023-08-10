# VIDEO: Algorithm Ladder #01: Basic Array

# Write a function that returns the sum of all numbers in a given array.

# NOTE: Do not use any built-in language functions that do this automatically for you.

# Input: [1, 2, 3, 4]
# Output: 10

# Explanation: (1 + 2 + 3 + 4) = 10

def total(array):
  sum = 0

  for number in array:
    sum += number

  return sum

print(total([1, 2, 3, 4]))