#!/usr/bin/node
const fs = require('fs');

const filePath = 'path/to/your/file.js';

fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }

    const updatedData = data.replace(/myVar\s*=\s*\d+/, 'myVar = 333');

    fs.writeFile(filePath, updatedData, 'utf8', (err) => {
        if (err) {
            console.error(err);
            return;
        }
        console.log('File updated successfully!');
    });
});
