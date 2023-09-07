# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def palindromic(number1, number2)
  largest_palindrome = 0

  (number1..999).each do |n|
    (number2..999).each do |n2|
      total = n * n2
      if total == total.to_s.reverse.to_i && total > largest_palindrome
        largest_palindrome = total
      end
    end
  end
    return largest_palindrome
end

p palindromic(231, 456)