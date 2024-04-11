#!/usr/bin/node

// Converts a givn numbe ftom base 10 to another base
exports.converter = function (base) { return num => num.toString(base); };
