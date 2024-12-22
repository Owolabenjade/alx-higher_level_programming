#!/usr/bin/node
const fs = require('fs');

const [,, sourceFile1, sourceFile2, destinationFile] = process.argv;

try {
  const content1 = fs.readFileSync(sourceFile1, 'utf8');
  const content2 = fs.readFileSync(sourceFile2, 'utf8');
  fs.writeFileSync(destinationFile, content1 + content2);
} catch (error) {
  console.error(error);
}