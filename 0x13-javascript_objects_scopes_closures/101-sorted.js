#!/usr/bin/node
const dict = require('./101-data').dict;

const occurrencesDict = {};

// Group user ids by occurrences
Object.entries(dict).forEach(([userId, occurrences]) => {
	if (!occurrencesDict[occurrences]) { 
	occurrencesDict[occurrences] = [];
	}
	occurrencesDict[occurrences].push(userId);
});

// Output the result
console.log(occurrencesDict);

