const fs = require('fs')

const nums = fs.readFileSync('./data', 'utf8').split("\n").map(num => +num).sort((a,b) => a-b)
nums.push(nums[nums.length - 1] + 3)

console.log(nums)
let result = nums.reduce((acc, num, idx, arr) => {
    let diff = idx === 0 ? num : num - arr[idx-1]
    console.log(diff)
    acc[diff]++
    return acc
}, [0, 0, 0, 0])
console.log(result)
console.log(result[1] * result[3])
