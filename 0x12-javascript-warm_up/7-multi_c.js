#!/usr/bin/node
const arg1 = process.argv[2];
const numOccurrences = parseInt(arg1);

if (isNaN(numOccurrences)) {
    console.log("Missing number of occurrences");
} else {
    for (let i = 0; i < numOccurrences; i++) {
        console.log("C is fun");
    }
}
