#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (num) {
  const toPrint = 'My number: ' + num;
  console.log(toPrint);
} else {
  console.log('Not a number');
}
