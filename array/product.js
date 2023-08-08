// Write a function that accepts an array of numbers and returns the product of all the numbers.

// Input: [1, 2, 3, 4]
// Output: 24

// Explanation: (1 x 2 x 3 x 4) = 24

function total(array) {
  let product = 1;

  array.forEach(function (number) {
    product *= number;
  });
  return product;
}

console.log(total([1, 2, 3, 4]));
