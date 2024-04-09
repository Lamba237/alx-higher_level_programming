#!/usr/bin/node

/*
 * A script that prints two arguments passed
 * to it, in the format "is"
 */
if (process.argv[3]) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else if (process.argv[2]) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
