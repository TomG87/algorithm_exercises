# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def palindromic(number1, number2):
    largest_palindrome = 0

    n = 1
    while n < number1:
        n2 = 1
        while n2 < number2:
            total = n * n2
            if str(total) == str(total)[::-1] and total > largest_palindrome:
                largest_palindrome = total
            n2 += 1
        n += 1

    return largest_palindrome

print(palindromic(999, 999))