#!/usr/bin/node
const a = parseInt(process.argv[2]);
function factorial (a) {
  if (isNaN(a)) {
    return 1;
  }
  if (a === 1) {
    return 1;
  }
  if (a > 1) {
    return a * factorial(a - 1);
  }
}
console.log(factorial(a));
