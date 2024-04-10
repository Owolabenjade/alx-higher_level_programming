#!/usr/bin/node
let count = 0; // Initialize a counter variable outside the function

exports.logMe = function (item) {
	console.log(`${count}: ${item}`);
	count++;
};

