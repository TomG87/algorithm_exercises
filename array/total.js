function total(array) {
  let sum = 0;

  array.forEach(function (number) {
    sum += number;
  });
  return sum;
}

console.log(total([1, 2, 3, 4]));
