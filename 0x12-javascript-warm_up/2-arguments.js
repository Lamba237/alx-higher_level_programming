#!/usr/bin/node

/* A script that checks if an argument was passd
 * in the console
 */
if (process.argv[3]) {
  console.log('Arguments found');
} else if (process.argv[2]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
