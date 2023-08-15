# Write a function that returns the greatest value from an array of numbers.

# Input: [5, 17, -4, 20, 12]
# Output: 20

# (After you complete the exercise successfully, I recommend watching this video: Think Like a Software Engineer Episode #50)

def highest(array):
    most = array[0]

    for number in array:
        if number > most:
            most = number

    return most

print(highest([5, 17, -4, 20, 12]))