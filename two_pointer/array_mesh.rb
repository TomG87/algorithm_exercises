# Given two arrays of strings, return a new string that contains every combination of a string from the first array concatenated with a string from the second array.

# Input: ["a", "b", "c"], ["d", "e", "f", "g"]
# Output: ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"]

def mesh(array, array2)

  new = []

  array.each do |one|
    array2.each do |two|
      new << (one + two)
    end
  end

  return new
end

p mesh(["a", "b", "c"], ["d", "e", "f", "g"])