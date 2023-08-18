// Given a string, write a function that returns true if the “$” character is contained within the string or false if it is not.

// Input: “i hate $ but i love money i know i know im crazy”
// Output: true

// Input: “abcdefghijklmnopqrstuvwxyz”
// Output: false

function money(string) {
  if (string.includes("$")) {
    return true;
  } else {
    return false;
  }
}

console.log(money("i hate $ but i love money i know i know im crazy"));
