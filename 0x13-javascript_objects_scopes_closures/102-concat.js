#!/usr/bin/node
const fs = require('fs');
const [,, fileA, fileB, destFile] = process.argv; // Destructure command-line arguments

fs.readFile(fileA, 'utf-8', (err, dataA) => {
	if (err) {
	console.error(err); 
	} else {
	fs.readFile(fileB, 'utf-8', (err, dataB) => {
	  if (err) {
		console.error(err); 
	  } else {
		fs.writeFile(destFile, dataA + dataB, (err) => {
		  if (err) {
			console.error(err); 
		  }
		});
	  }
	});
	}
});

