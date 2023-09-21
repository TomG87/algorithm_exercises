// Given an array of strings, return a hash that provides of a count of how many times each string occurs.

// Input: ["Dewey", "Truman", "Dewey", "Dewey", "Truman", "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]

// Output: {"Dewey" => 6, "Truman" => 5}

// Explanation: "Dewey" occurs 6 times in the array, while "Truman" occurs 5 times.

function count(string) {
  let i = 0;
  let most = {};

  while (i < string.length) {
    if (most[string[i]]) {
      most[string[i]] += 1;
    } else {
      most[string[i]] = 1;
    }
    i += 1;
  }
  return most;
}

console.log(
  count([
    "Dewey",
    "Truman",
    "Dewey",
    "Dewey",
    "Truman",
    "Truman",
    "Dewey",
    "Truman",
    "Truman",
    "Dewey",
    "Dewey",
  ])
);
