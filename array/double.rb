# Given an array of numbers, write a function that returns a new array whose values are the original array’s value doubled.

# Input: [4, 2, 5, 99, -4]
# Output: [8, 4, 10, 198, -8]

def double(array)
  new_array = []

  array.each do |number|
    new_array << (number * 2)
  end

  return new_array
end

p double([4, 2, 5, 99, -4])