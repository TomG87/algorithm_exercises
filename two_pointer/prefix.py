# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

def prefix(array):

  i = 0
  count = 0

  while i < len(array):
    if array[0][i] == array[1][i] and array[0][i] == array[2][i] and array[1][i] == array[2][i]:
      count += 1
    i += 1

  if count > 1:
    return count
  else:
    return ""

print(prefix(["flower","flow","flight"]))