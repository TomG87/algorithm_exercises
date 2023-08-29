# Write a function that prints out every number from 1 to N, with the following exceptions:

# If the number is divisible by 3, print out "FIZZ".
# If the number is divisible by 5, print out "BUZZ".
# If the number is divisible by both 3 and 5, print out "FIZZBUZZ".

def fizzbuzz(number):
    if number % 5 == 0 and number % 3 == 0:
      return "FIZZBUZZ"
    else:
       if number % 5 == 0:
          return "BUZZ"
       else:
          if number % 3 == 0:
             return "FIZZ"
          else:
             return f"{number} is not divisible"
          
print(fizzbuzz(11))
  
