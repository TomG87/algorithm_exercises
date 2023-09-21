# Given a string, find the most commonly occurring letter.

# Input: “peter piper picked a peck of pickled peppers”
# Output: “p”

def basic(string)

  letters = {}
  i = 0
  most_count = 0
  most_letters = ""

  while i < string.length
    if letters[string[i]]
      letters[string[i]] += 1
    else
      letters[string[i]] = 1
    end
    if letters[string[i]] > most_count
      most_count = letters[string[i]]
      most_letters = string[i]
    end
    i += 1  
  end

  return most_letters
end

p basic("peter piper picked a peck of pickled peppers")