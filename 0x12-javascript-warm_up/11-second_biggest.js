#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const argString = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(argString[argString.length - 2]);
}
