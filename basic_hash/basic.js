// # Given a string, find the most commonly occurring letter.

// # Input: “peter piper picked a peck of pickled peppers”
// # Output: “p”

function basic(string) {
  let letters = {};
  let i = 0;
  let mostCount = 0;
  let mostLetters = "";

  while (i < string.length) {
    if (letters[string[i]]) {
      letters[string[i]] += 1;
    } else {
      letters[string[i]] = 1;
    }
    if (letters[string[i]] > mostCount) {
      mostCount = letters[string[i]];
      mostLetters = string[i];
    }
    i += 1;
  }
  return mostLetters;
}

console.log(basic("peter piper picked a peck of pickled peppers"));
