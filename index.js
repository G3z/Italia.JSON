var short = require('./italia.json');
var complete = require('./italia_comuni.json');

short.comuni = complete;

module.exports = short;