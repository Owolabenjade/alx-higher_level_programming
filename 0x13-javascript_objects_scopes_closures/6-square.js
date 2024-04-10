#!/usr/bin/node
const Square = require('./5-square');

class Square extends Square { // Inherit from 'Square' in 5-square.js
	charPrint(c) {
		if (typeof c === 'undefined') {
			c = 'X';
		}
		for (let i = 0; i < this.height; i++) { 
			console.log(c.repeat(this.width));
		}
	}
}

