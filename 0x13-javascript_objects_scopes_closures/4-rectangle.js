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

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
