# Given two sorted arrays, merge the second array into the first array while ensuring that the first array remains sorted. Do not use any built-in sort methods.

# Input :
# A : [1, 5, 8]
# B : [6, 9]

# Modified A : [1, 5, 6, 8, 9]

def sorted(array, array2):

  i = 0
  i2 = 0
  merged = []

  while i < len(array) and i2 < len(array2):
    if array[i] < array2[i2]:
      merged.append(array[i])
      i += 1
    else:
      merged.append(array2[i2])
      i2 += 1
  
  while i < len(array):
    merged.append(array[i])
    i += 1

  while i2 < len(array2):
    merged.append(array2[i2])
    i2 += 1

  return merged

print(sorted([1, 5, 8], [6, 9]))
