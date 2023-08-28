def prime(number):
  i = 2

  while i < number:
    if number % i == 0:
      return f"{number} is not a prime number"
    i += 1

  else:
    return f"{number} is a prime number"

print(prime(8))