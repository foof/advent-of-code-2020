const fs = require('fs')

const pps = fs.readFileSync('./data', 'utf8').split("\n\n").map(pp => pp.replace(/\n/g, ' '))
const required = [
    { field: 'byr', validator: (val) => val.match(/^[0-9]{4}$/) && Math.min(Math.max(parseInt(val), 1920), 2002) === parseInt(val)},
    { field: 'iyr', validator: (val) => val.match(/^[0-9]{4}$/) && Math.min(Math.max(parseInt(val), 2010), 2020) === parseInt(val)},
    { field: 'eyr', validator: (val) => val.match(/^[0-9]{4}$/) && Math.min(Math.max(parseInt(val), 2020), 2030) === parseInt(val)},
    { field: 'hgt', validator: (val) => {
        if (!val.match(/^[0-9]*(cm|in)$/)) {
            return false
        }
        const intVal = parseInt(val.replace(/\D/, ''))
        if (val.match(/cm/)) {
            return Math.min(Math.max(intVal, 150), 193) === intVal
        } else if (val.match(/in/)) {
            return Math.min(Math.max(intVal, 59), 76) === intVal
        }
    }},
    { field: 'hcl', validator: (val) => val.match(/^#[0-9a-z]{6}$/)},
    { field: 'ecl', validator: (val) => val.match(/^(amb|blu|brn|gry|grn|hzl|oth)$/)},
    { field: 'pid', validator: (val) => val.match(/^[0-9]{9}$/)},
]

console.log(pps.filter(pp => {
    const ppObj = {}
    pp.split(' ').forEach(i => {
        const [field, value] = i.split(':')
        ppObj[field] = value
    })
    for ({ field, validator } of required) {
        if (!Object.keys(ppObj).includes(field) || !validator(ppObj[field])) {
            return false
        }
    }
    return true
}).length)