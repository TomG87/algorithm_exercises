// #Given an array of numbers, write a function that returns a new array that contains all numbers from the original array that are less than 100.

// # Input: [99, 101, 88, 4, 2000, 50]
// # Output: [99, 88, 4, 50]

function lessThan(array) {
  let new_array = [];

  array.forEach(function (number) {
    if (number < 100) {
      new_array.push(number);
    }
  });
  return new_array;
}

console.log(lessThan([99, 101, 88, 4, 2000, 50]));
