// # Given two arrays of strings, return a new string that contains every combination of a string from the first array concatenated with a string from the second array.

// # Input: ["a", "b", "c"], ["d", "e", "f", "g"]
// # Output: ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"]

function mesh(array, array2) {
  let newArray = [];

  array.forEach(function (one) {
    array2.forEach(function (two) {
      newArray.push(one + two);
    });
  });
  return newArray;
}

console.log(mesh(["a", "b", "c"], ["d", "e", "f", "g"]));
