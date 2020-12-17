const fs = require('fs')

const bagMap = {};
const bags = fs.readFileSync('./data', 'utf8')
    .split("\n")
    .map(bag => bag.replace('.', ''))
    .map(bag => bag.replace(/bags/g, 'bag'))
    .map(bag => bag.replace(/\d /g, ''))
    .map(bag => bag.split(" contain "))
    .map(bag => [bag[0], bag[1].split(', ')])

bags.forEach(bag => bagMap[bag[0]] = bag[1])



const bagCanContain = (searchingInBag, bagToFind) => {
    // console.log(`Searching for ${bagToFind} in ${searchingInBag}`)
    if (!bagMap[searchingInBag] || bagMap[searchingInBag][0] === 'no other bag') {
        return false
    }
    if (bagMap[searchingInBag].includes(bagToFind)) {
        return true
    }
    for (bag of bagMap[searchingInBag]) {
        if (bagCanContain(bag, bagToFind)) {
            return true
        }
    }
    return false
}

const result = Object.keys(bagMap).map(bag => bagCanContain(bag, 'shiny gold bag')).filter(i => i)

console.log(result.length)
