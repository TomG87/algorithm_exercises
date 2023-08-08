// Write a function that returns the greatest value from an array of numbers.

// Input: [5, 17, -4, 20, 12]
// Output: 20

// (After you complete the exercise successfully, I recommend watching this video: Think Like a Software Engineer Episode #50)

function max(array) {
  let highest = array[0];

  array.forEach(function (number) {
    if (number > highest) highest = number;
  });
  return highest;
}

console.log(max([5, 17, -4, 20, 12]));
