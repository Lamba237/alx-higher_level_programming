#!/usr/bin/node
const occurrence = parseInt(process.argv[2]);

if (isNaN(occurrence)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < occurrence; i++) {
    console.log('C is fun');
  }
}
