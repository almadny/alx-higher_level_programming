#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (size) {
  for (let j = 0; j < size; j++) {
    let str1 = '';
    for (let i = 0; i < size; i++) {
      str1 += 'X';
    }
    console.log(str1);
  }
} else {
  console.log('Missing size');
}
