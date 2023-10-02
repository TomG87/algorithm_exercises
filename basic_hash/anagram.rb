# Given two strings, return true if they are anagrams of each other, and false if they are not. An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

# Do not use any built-in sort methods.

# Input: “silent”, “listen”
# Output: true

# Input: “frog”, “bear”
# Output: false

def anagram(string, string2)

  i = 0
 
  if string.length == string2.length
    while i < string.length
      string2.each_char do |letter|
        if string[0..-1].include?(letter)
          i += 1
        else
          return false
        end
      end   
    end
  else
    return false
  end
  return true
end

p anagram("silent", "listen")
