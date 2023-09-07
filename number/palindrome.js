// # A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

// # Find the largest palindrome made from the product of two 3-digit numbers.

function palindromic(number1, number2) {
  var largest_palindrome = 0;

  for (var n = 1; n <= number1; n++) {
    for (var n2 = 1; n2 <= number2; n2++) {
      var total = n * n2;
      var reversedTotal = parseInt(
        total.toString().split("").reverse().join("")
      );

      if (total === reversedTotal && total > largest_palindrome) {
        largest_palindrome = total;
      }
    }
  }

  return largest_palindrome;
}

console.log(palindromic(999, 999));
