# Given a string, write a function that returns a copy of the original string that has every other character capitalized. (Capitalization should begin with the second character.)

# Input: “hello, how are your porcupines today?”
# Output: “hElLo, HoW ArE YoUr pOrCuPiNeS ToDaY?”

def alternate(string)
  i = 0
  i2 = 1
  upper = ""

  while i < string.length
    upper += string[i]
    if i2 < string.length
      upper += string[i2].capitalize 
    end
    i += 2
    i2 += 2
  end

  return upper
end

p alternate("hello, how are your porcupines today?")





