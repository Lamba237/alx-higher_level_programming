#!/usr/bin/node

// Outputs a number converted
const num = Number(process.argv[2]);

if (!num) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
