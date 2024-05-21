#!/usr/bin/node
// a script that prints the number of movies where
// the character “Wedge Antilles” is present.
const request = require('request');
const url = process.argv[2];
const movieId = 18;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < data.results.length; i++) {
    if (data.results[i].characters.includes(`https://swapi-api.alx-tools.com/api/people/${movieId}/`)) {
      count++;
    }
  }
  console.log(count);
});
