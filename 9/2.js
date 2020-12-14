const fs = require('fs')

const nums = fs.readFileSync('./data', 'utf8').split("\n").map(num => parseInt(num))

const findSumPair = (sum, arr) => {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length; j++) {
            if (arr[i] === arr[j]) continue
            if (arr[i] + arr[j] === sum) return [arr[i], arr[j]]
        }
    }
    return false
}

const preamble = 25
const result = nums.reduce((acc, num, idx, src) => {
    if (acc) return acc
    if (idx < preamble) return acc

    const sumPair = findSumPair(num, src.slice(idx - preamble, idx), preamble)
    return sumPair ? acc : num
}, false)

if (!result) {
    process.exit()
}

const findContSet = (num, arr) => {
    for (let i = 0; i < arr.length; i++) {
        let sum = arr[i]

        for (let end = i + 1; end < arr.length; end++) {
            sum += arr[end]

            if (sum === num) {
                return [i, end]
            } else if (sum > num) {
                break
            }
        }
    }
    return false
}

const set = findContSet(result, nums)
if (set) {
    const subNums = nums.slice(set[0], set[1] + 1).sort((a, b) => a - b)
    console.log(subNums[0] + subNums[subNums.length - 1])
}