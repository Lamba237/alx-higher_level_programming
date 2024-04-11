#!/usr/bin/node

// A script that imports an Array an computes a new one

const list = require('./100-data.js').list;
console.log(list);
console.log(list.map((item, index) => item * index));
