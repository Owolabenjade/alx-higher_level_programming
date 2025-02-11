#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
	  console.log(err);
  } else if (response.statusCode === 200) {
	  const films = JSON.parse(body);
	  let count = 0;
	  films.results.forEach((film) => {
		  if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
			  count++;
		  }
	  });
	  console.log(count);
  } else {
	  console.log(`Error: ${response.statusCode}`);
  }
});
