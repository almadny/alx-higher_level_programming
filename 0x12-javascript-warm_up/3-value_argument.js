#!/usr/bin/node
let i = 2;
while (process.argv[i]) {
  console.log(process.argv[i]);
  i++;
}
if (i < 3) {
  console.log('No argument');
}
