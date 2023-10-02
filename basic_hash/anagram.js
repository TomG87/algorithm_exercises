// Given two strings, return true if they are anagrams of each other, and false if they are not. An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

// Do not use any built-in sort methods.

// Input: “silent”, “listen”
// Output: true

// Input: “frog”, “bear”
// Output: false

function anagram(string, string2) {
  let i = 0;

  if (string.length === string2.length) {
    while (i < string.length) {
      if (string.includes(string2[i])) {
        i += 1;
      } else {
        return false;
      }
      return true;
    }
  } else {
    return false;
  }
}
console.log(anagram("silent", "listen"));
