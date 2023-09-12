#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (v) {
    if (v === undefined) {
      v = 'X';
    }
    for (let n = 0; n < this.height; n++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
