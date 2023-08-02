# Write a function that returns the greatest value from an array of numbers.

# Input: [5, 17, -4, 20, 12]
# Output: 20

# (After you complete the exercise successfully, I recommend watching this video: Think Like a Software Engineer Episode #50)

def max(array)
  largest = array[0]

  array.each do |number|
    if number > largest
      largest = number
    end
  end

  return largest
end

p max([5, 17, -4, 8, 12])