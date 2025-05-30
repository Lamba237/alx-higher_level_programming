#!/usr/bin/node
// script that prints the title of a Star Wars
// movie where the episode number matches a given integer.
const request = require('request');
const argument = process.argv;

const movieId = argument[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(JSON.parse(body).title);
});
