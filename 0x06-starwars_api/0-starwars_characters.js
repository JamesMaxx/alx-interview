#!/usr/bin/node

const argv = process.argv;
const urlFilm = "https://swapi-api.hbtn.io/api/films/";
const urlMovie = `${urlFilm}${argv[2]}/`;

const request = require("request");

request(urlMovie, function (error, response, body) {
  if (error == null) {
    const fbody = JSON.parse(body);
    const characters = fbody.characters;

    if (characters && characters.length > 0) {
      characters.forEach((charUrl) => {
        request(charUrl, function (error, response, body) {
          if (!error) {
            const rbody = JSON.parse(body);
            console.log(rbody.name);
          } else {
            console.error("error:", error);
          }
        });
      });
    }
  } else {
    console.log(error);
  }
});
