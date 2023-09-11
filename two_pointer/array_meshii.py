# Given ONE array of strings, return a new array that contains every combination of each string with every other string in the array.

# Input: ["a", "b", "c", "d"]
# Output: ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"]

def mesh (array):

  newArray = []
  i = 0

  while i < len(array):
    for letter in array:
      if letter != array[i]:
        newArray.append(array[i] + letter)
    i += 1

  return newArray

print(mesh(["a", "b", "c", "d"]))