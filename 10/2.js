const fs = require('fs')

const nums = fs.readFileSync('./data', 'utf8').split("\n").map(num => +num).sort((a,b) => a-b)
nums.push(nums[nums.length - 1] + 3)

const dp = {}

const solve = (nums, idx, prevIdx) => {
    let num = nums[idx]
    let prevNum = prevIdx === false ? 0 : nums[prevIdx]
    let key = `${num},${prevNum || ''}`

    if (dp[key]) {
        return dp[key] // Already in memory
    }

    if (num - prevNum <= 3) {
        if (idx === nums.length - 1) {
            return 1 // New path found
        } else {
            dp[key] = solve(nums, idx + 1, idx) + solve(nums, idx + 1, prevIdx)
        }
    } else {
        dp[key] = 0
    }

    return dp[key]
}

console.log(solve(nums, 0, false))
