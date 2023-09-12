#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (e) {
    if (e === undefined) {
      e = 'X';
    }
    for (let n = 0; n < this.height; n++) {
      let z = '';
      for (let k = 0; k < this.width; k++) {
        z += e;
      }
      console.log(z);
    }
  }
}

module.exports = Square;
