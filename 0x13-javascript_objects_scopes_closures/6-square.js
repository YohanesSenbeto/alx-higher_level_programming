#!/usr/bin/node
const SquareP = require('./5-square')

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X'
    }

    if (!this.width || !this.height) {
      console.log('Empty square')
      return
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width))
    }
  }
}
module.exports = Square
