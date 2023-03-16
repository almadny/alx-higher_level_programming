#!/usr/bin/node
let first = -1;
let second = -1;
const arrSize = process.argv.length;
if (arrSize > 3) {
  for (let a = 2; a < arrSize; a++) {
    const arrElement = process.argv[a];
    if (arrElement > first) {
      second = first;
      first = arrElement;
    } else if (arrElement > second) {
      second = arrElement;
    }
  }
  console.log(second);
} else {
  console.log(0);
}
