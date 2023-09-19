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

def common(array)

  count = 0
  i = 0


  while i < array.length
    if array[0][i] == array[1][i] && array[0][i] == array[2][i] && array[1] [i]== array[2][i]
      count += 1
    end
  i += 1
  end

  if count > 1
    return count
  else
    return ""
  end
end

p common(["flower","flow","flight"])
