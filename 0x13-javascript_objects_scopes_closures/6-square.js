#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (this.width && this.height) {
      const printChar = c === undefined ? 'X' : c;
      for (let i = 0; i < this.height; i++) {
        console.log(printChar.repeat(this.width));
      }
    }
  }
}

module.exports = Square;