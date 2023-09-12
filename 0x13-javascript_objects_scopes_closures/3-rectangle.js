#!/usr/bin/node
class Rectangle {
  constructor (c, b) {
    if ((c > 0) && (b > 0)) {
      this.width = c;
      this.height = b;
    }
  }

  print () {
    for (let n = 0; n < this.height; n++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
