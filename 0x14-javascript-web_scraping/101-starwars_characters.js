#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    if (response.headers['content-type'].startsWith('application/json')) {
      const movie = JSON.parse(body);
      const characterUrls = movie.characters;

      const fetchCharacter = (url) => {
        request.get(url, function (error, response, body) {
          if (error) {
            console.error(error);
          } else {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      };

      characterUrls.forEach(fetchCharacter);
    } else {
      console.error('Invalid response: Expected JSON but received HTML');
    }
  }
});
