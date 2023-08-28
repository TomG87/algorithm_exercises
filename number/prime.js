function prime(number) {
  let i = 2;

  while (i < number) {
    if (number % i === 0) {
      return `${number} is not a prime number`;
    }
    i++;
  }

  return `${number} is a prime number`;
}

console.log(prime(8));
