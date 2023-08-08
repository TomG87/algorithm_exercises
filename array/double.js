// Given an array of numbers, write a function that returns a new array whose values are the original array’s value doubled.

// Input: [4, 2, 5, 99, -4]
// Output: [8, 4, 10, 198, -8]

function twice(array) {
  let new_array = [];

  array.forEach(function (number) {
    new_array.push(number * 2);
  });
  return new_array;
}

console.log(twice([4, 2, 5, 99, -4]));
