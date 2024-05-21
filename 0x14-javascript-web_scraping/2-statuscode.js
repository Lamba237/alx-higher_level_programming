#!/usr/bin/node
// This script displays that status code of a GET request
const request = require('request');
const argument = process.argv;

request(argument[2], (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code: ' + response.statusCode);
});
