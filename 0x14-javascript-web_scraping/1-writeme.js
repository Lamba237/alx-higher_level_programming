#!/usr/bin/node
// a script that writes a string to a file
const fs = require('fs');
const argument = process.argv;

fs.writeFile(argument[2], argument[3], 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
