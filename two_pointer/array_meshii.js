// # Given ONE array of strings, return a new array that contains every combination of each string with every other string in the array.

// # Input: ["a", "b", "c", "d"]
// # Output: ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"]

function mesh(array) {
  let newArray = [];
  let i = 0;

  while (i < array.length) {
    array.forEach(function (letter) {
      if (letter !== array[i]) {
        newArray.push(array[i] + letter);
      }
    });
    i += 1;
  }
  return newArray;
}

console.log(mesh(["a", "b", "c", "d"]));
