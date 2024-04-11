#!/usr/bin/node
const args = process.argv.slice(2); // Slice off the first two elements to get only the arguments

console.log(`${args[0] || 'undefined'} is ${args[1] || 'undefined'}`);

