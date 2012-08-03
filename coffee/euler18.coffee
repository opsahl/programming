#require filesystem
fs = require 'fs'

#Read in triangle
fileText = fs.readFileSync('euler18.txt').toString()

console.out fileText
