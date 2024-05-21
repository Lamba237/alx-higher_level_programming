#!/usr/bin/node
// a script that reads and prints the content of a file.
const fs = require('fs');
const argument = process.argv;

fs.readFile(argument[2], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
