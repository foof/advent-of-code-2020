const fs = require('fs')

const pps = fs.readFileSync('./data', 'utf8').split("\n\n").map(pp => pp.replace(/\n/g, ' '))
const required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

console.log(pps.filter(pp => {
    const present = pp.split(' ').map(i => i.split(':')[0])
    return required.filter(req => !present.includes(req)).length === 0
}).length)