# Given two arrays of strings, return a new string that contains every combination of a string from the first array concatenated with a string from the second array.

# Input: ["a", "b", "c"], ["d", "e", "f", "g"]
# Output: ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"]

def mesh(array, array2):

  newArray = []

  for one in array:
    for two in array2:
      newArray.append(one + two)

  return newArray

print(mesh(["a", "b", "c"], ["d", "e", "f", "g"]))


