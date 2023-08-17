// Write a function that returns the reverse of a given string.

// Input: “abcde”
// Output: “edcba”

function backwards(string) {
  return string.split("").reverse().join("");
}

console.log(backwards("abcde"));
