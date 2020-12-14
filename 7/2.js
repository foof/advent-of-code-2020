const fs = require('fs')

const bagMap = {};
const bags = fs.readFileSync('./data', 'utf8')
    .split("\n")
    .map(bag => bag.replace('.', ''))
    .map(bag => bag.replace(/ bags?/g, ''))
    .map(bag => bag.split(" contain "))
    .map(bag => [ bag[0], bag[1].split(', ')
        .filter(b => b !== 'no other')
        .map(b => ({
            count: parseInt(b.split(' ')[0]),
            name: b.split(' ').splice(1).join(' ')
        })
    )])

bags.forEach(bag => bagMap[bag[0]] = bag[1])

let count = 0
const countContainingBags = (searchBag) => {
    if (!bagMap[searchBag] || !bagMap[searchBag].length) {
        return
    }
    for (const bag of bagMap[searchBag]) {
        count += bag.count
        for (let i = 0; i < bag.count; i++) {
            countContainingBags(bag.name)
        }
    }
}
countContainingBags('shiny gold')

console.log(count)