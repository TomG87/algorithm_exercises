
# Given an array of numbers, return true if the array is a "100 Coolio Array", or false if it is not.

# A "100 Coolio Array" meets the following criteria:

# Its first and last numbers add up to 100,
# Its second and second-to-last numbers add up to 100,
# Its third and third-to-last numbers add up to 100,
# and so on and so forth.

# Here are examples of 100 Coolio Arrays:

# [1, 2, 3, 97, 98, 99]
# [90, 20, 70, 100, 30, 80, 10]

def coolio(array)

  length = (array.length/2)
  i = 0
  j = -1

  while i < length
    total = (array[i] + array[j])
    if total != 100
      return False
    end
    i += 1
    j -= 1
  end
  return "Coolio Array"
end

p coolio([1, 2, 3, 97, 98, 99])