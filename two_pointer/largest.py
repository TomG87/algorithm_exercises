# Find the largest product of any two numbers within a given array.

# Input: [5, -2, 1, -9, -7, 2, 6]
# Output: 63 (-9 * -7)

def largest(array):

  i = 0
  i2 = 1
  max = array[i] * array[i2]

  while i2 < len(array):
    total = array[i] * array[i2]
    if total > max:
       max = total
    i += 1
    i2 += 1

  return max


print(largest([5, -2, 1, -9, -7, 2, 6]))