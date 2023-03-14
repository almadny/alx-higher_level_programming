#!/usr/bin/node
let xtimes = parseInt(process.argv[2]);
if (xtimes) {
  if (xtimes > 0) {
    while (xtimes--) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurences');
}
