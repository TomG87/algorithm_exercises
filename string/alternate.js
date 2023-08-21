// Given a string, write a function that returns a copy of the original string that has every other character capitalized. (Capitalization should begin with the second character.)

// Input: “hello, how are your porcupines today?”
// Output: “hElLo, HoW ArE YoUr pOrCuPiNeS ToDaY?”

function alternate(string) {
  let i = 0;
  let i2 = 1;
  let upper = "";

  while (i < string.length) {
    upper += string[i];
    if (i2 < string.length) {
      upper += string[i2].toUpperCase();
    }
    i += 2;
    i2 += 2;
  }
  return upper;
}

console.log(alternate("hello, how are your porcupines today?"));
