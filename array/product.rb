# Write a function that accepts an array of numbers and returns the product of all the numbers.

# Input: [1, 2, 3, 4]
# Output: 24

# Explanation: (1 x 2 x 3 x 4) = 24

def total(array)
  sum = 1

  array.each do |number|
    sum *= number
  end

  return sum
end

p total([1, 2, 3, 4])