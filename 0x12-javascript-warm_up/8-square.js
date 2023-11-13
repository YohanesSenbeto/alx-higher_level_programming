#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (isNaN(size))
    console.log("Missing size");
else if (size <= 0)
    console.log("Size must be a positive number");
else
    console.log(Array(size).fill("X".repeat(size)).join("\n"));
