#!/usr/bin/node
let numArguments = 0

exports.logMe = function (item) {
  console.log(`${numArguments}: ${item}`)
  numArguments++
}
