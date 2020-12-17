const fs = require('fs')

const groups = fs.readFileSync('./data', 'utf8').split("\n\n").map(group => group.split("\n").map(person => person.split('')))

const results = groups
    .map(group => group.reduce((set, person) => {
        person.forEach(q => set.add(q))
        return set
    }, new Set()))
    .map(set => set.size)
    .reduce((acc, count) => acc + count)


console.log(results)