# Given ONE array of strings, return a new array that contains every combination of each string with every other string in the array.

# Input: ["a", "b", "c", "d"]
# Output: ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"]

def mesh(array)

  new_array = []
  i = 0

  while i < array.length
    array.each do |letter|
      if letter != array[i]
        new_array<< (array[i] + letter)
      end
    end
    i += 1
  end
  return new_array
end

p mesh(["a", "b", "c", "d"])