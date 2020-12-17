const fs = require('fs')

const nums = fs.readFileSync('./data', 'utf8').split("\n").map(num => parseInt(num))

const preamble = 25

const findSumPair = (sum, arr) => {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length; j++) {
            if (i === j) continue
            if (arr[i] + arr[j] === sum) return [arr[i], arr[j]]
        }
    }
    return false
}

const result = nums.reduce((acc, num, idx, src) => {
    if (acc) return acc
    if (idx < preamble) return acc

    const sumPair = findSumPair(num, src.slice(idx - preamble, idx))
    return sumPair ? acc : num
}, false)

console.log(result)