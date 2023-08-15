# Given an array of numbers, write a function that returns a new array whose values are the original array’s value doubled.

# Input: [4, 2, 5, 99, -4]
# Output: [8, 4, 10, 198, -8]

def double(array):
    newArray = []

    for number in array:
      newArray.append(number*2)
    
    return newArray

print(double([4, 2, 5, 99, -4]))