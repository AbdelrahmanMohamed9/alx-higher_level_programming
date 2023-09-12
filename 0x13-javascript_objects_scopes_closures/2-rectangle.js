#!/usr/bin/node
class Rectangle {
  constructor (c, b) {
    if ((c > 0) && (b > 0)) {
      this.width = c;
      this.height = b;
    }
  }
}

module.exports = Rectangle;
