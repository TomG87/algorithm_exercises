// Given a string, write a function that returns the first occurence of two duplicate characters in a row, and return the duplicated character.

// Input: “abcdefghhijkkloooop”
// Output: “h”

function duplicate(string) {
  let i = 0;
  let i2 = 1;

  while (i < string.length) {
    if (string[i] === string[i2]) {
      return string[i];
    } else {
      i += 1;
      i2 += 1;
    }
  }
}

console.log(duplicate("abcdefghhijkkloooop"));
