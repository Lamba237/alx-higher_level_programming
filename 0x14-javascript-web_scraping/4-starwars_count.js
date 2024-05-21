#!/usr/bin/node
// This script prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < data.results.length; i++) {
    if (data.results[i].characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      count++;
    }
  }
  console.log(count);
});
