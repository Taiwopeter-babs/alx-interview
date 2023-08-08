#!/usr/bin/node
const request = require('request');

/**
 * Entry point of the module
 */
(function main () {
  const movieId = parseInt(process.argv.slice(-1), 10);

  getMovieChracters(movieId);
})();

/**
 * Get all characters from a star wars movie
 * @param {*} movieId - Id of the movie
 */
function getMovieChracters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  // make request
  request.get(url, function (error, response, body) {
    if (error) {
      throw new Error('Error with the request');
    }
    const charactersUrl = JSON.parse(body).characters;
    recurseThroughCharactersUrl(0, charactersUrl.length, charactersUrl);
  });
}

/**
 * A recursive function that requests the name of a star wars
 * character from the url.
 * @param {*} index - index of element in tha array
 * @param {*} arrayLength - array size
 * @param {*} array - array containing elements
 * @returns - nothing
 */
function recurseThroughCharactersUrl (index, arrayLength, array) {
  if (index === arrayLength) {
    return;
  }
  request.get(array[index], function (error, response, body) {
    if (error) {
      throw new Error(`Error with the request ${array[index]}`);
    }
    const characterName = JSON.parse(body).name;
    console.log(characterName);
    recurseThroughCharactersUrl(index + 1, arrayLength, array);
  });
}
