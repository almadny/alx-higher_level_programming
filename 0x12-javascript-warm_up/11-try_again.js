#!/usr/bin/node
const arr = process.argv.slice(2);
if (arr.length < 2) {
  console.log(0);
} else {
  const arrInt = arr.map(ele => parseInt(ele));
  const stArrInt = arrInt.sort((a, b) => b - a);
  console.log(stArrInt[1]);
}
