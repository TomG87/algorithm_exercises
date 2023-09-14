// Given two sorted arrays, merge the second array into the first array while ensuring that the first array remains sorted. Do not use any built-in sort methods.

// Input :
// A : [1, 5, 8]
// B : [6, 9]

// Modified A : [1, 5, 6, 8, 9]

function sorted(array, array2) {
  let i = 0;
  let i2 = 0;
  let merged = [];

  while (i < array.length && i2 < array2.length) {
    if ((array[i], array2[i2])) {
      merged.push(array[i]);
      i += 1;
    } else {
      merged.push(array2[i2]);
      i2 += 1;
    }
    while (i < array.length) {
      merged.push(array[i]);
      i += 1;
    }
    while (i2 < array2.length) {
      merged.push(array2[i2]);
      i2 += 1;
    }
  }
  return merged;
}

console.log(sorted([1, 5, 8], [6, 9]));
