const fs = require('fs')

const input = fs.readFileSync('./data', 'utf8').split("\n\n").map(group => group.split("\n").map(person => person.split('')))

console.log(input
    .map(group => group.reduce((acc, person) => person.filter(q => acc.includes(q))))
    .reduce((acc, qs) => acc + qs.length, 0))