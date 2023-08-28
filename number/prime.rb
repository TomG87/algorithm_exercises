# Description
# Write a function that returns whether a given number is a prime number.

def prime(number)
  i = 2  # Start from 2 since 1 is not considered prime

  while i < number
    if number % i == 0
      return "#{number} is not a prime number"
    end
    i += 1
  end

  return "#{number} is a prime number"
end

puts prime(23)