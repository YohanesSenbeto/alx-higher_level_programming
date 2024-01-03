#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;
    let charactersCount = 0;

    characterUrls.forEach(characterUrl => {
      request.get(characterUrl, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);

          charactersCount++;
          if (charactersCount === characterUrls.length) {// All characters have been printed
            process.exit();
          }
        }
      });
    });
  }
});