#!/usr/bin/node
const args = process.argv.slice(2).map(Number).filter(Number.isInteger);
const index = args.indexOf(12);

if (index !== -1) {
    args[index] = 89;
}

const result = args.length >= 2 ? args.sort((a, b) => b - a)[1] : 0;
console.log("The second biggest integer is:", result);
