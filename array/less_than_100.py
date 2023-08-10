# Given an array of numbers, write a function that returns a new array that contains all numbers from the original array that are less than 100.

# Input: [99, 101, 88, 4, 2000, 50]
# Output: [99, 88, 4, 50]

def lessThan(array):
    newArray = []

    for number in array:
      if number < 100:
         newArray.append(number)
    
    return newArray

print(lessThan([99, 101, 88, 4, 2000, 50]))
        