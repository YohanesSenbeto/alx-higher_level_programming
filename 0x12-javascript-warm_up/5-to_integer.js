#!/usr/bin/node
const arg1 = process.argv[2];
const convertedArg = parseInt(arg1);

if (!isNaN(convertedArg)) {
    console.log(`My number: ${convertedArg}`);
} else {
    console.log("Not a number");
}
