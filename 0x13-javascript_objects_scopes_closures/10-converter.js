#!/usr/bin/node
exports.converter = function (base) {
	const numerals = "0123456789ABCDEF"; // For bases up to 16

	return function (num) {
		let result = "";
		while (num > 0) {
			result = numerals[num % base] + result; 
			num = Math.floor(num / base);
		}
		return result || "0"; // Handle the case where num is 0
	};
};

