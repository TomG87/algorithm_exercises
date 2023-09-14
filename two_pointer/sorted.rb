# Description
# Given two sorted arrays, merge the second array into the first array while ensuring that the first array remains sorted. Do not use any built-in sort methods.

# Input :
# A : [1, 5, 8]
# B : [6, 9]

# Modified A : [1, 5, 6, 8, 9]

def sorted(array1, array2)
  merged_array = []
  i = 0
  j = 0

  while i < array1.length && j < array2.length
    if array1[i] < array2[j]
      merged_array << array1[i]
      i += 1
    else
      merged_array << array2[j]
      j += 1
    end
  end

  # If there are remaining elements in array1, add them
  while i < array1.length
    merged_array << array1[i]
    i += 1
  end

  # If there are remaining elements in array2, add them
  while j < array2.length
    merged_array << array2[j]
    j += 1
  end

  return merged_array
end

p sorted([1, 5, 8], [6, 9])
