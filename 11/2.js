const fs = require('fs')

const nums = fs.readFileSync('./data', 'utf8').split("\n").map(r => r.split(''))

const equal = (arr1, arr2) => JSON.stringify(arr1) === JSON.stringify(arr2)

const canSeeInDirection = (fi, fj, di, dj, state) => {
    const maxRow = state.length-1
    const maxCol = state[0].length-1
    let i = fi+di
    let j = fj+dj
    while (i >= 0 && j >= 0 && i <= maxRow && j <= maxCol) {
        if (state[i][j] === '#') {
            return true
        }
        if (state[i][j] === 'L') {
            return false
        }
        i += di
        j += dj
    }
    return false
}

const countVisible = (i, j, state) => {
    const maxRow = state.length-1
    const maxCol = state[0].length-1

    if (i > maxRow || j > maxCol) {
        console.log('outside bounds')
        process.exit(1)
    }

    let directions = [
        [-1, -1],
        [-1, 0],
        [-1, 1],

        [0, -1],
        // [0, 0],
        [0, 1],

        [1, -1],
        [1, 0],
        [1, 1],
    ]

    let count = 0
    for (dir of directions) {
        if (canSeeInDirection(i, j, dir[0], dir[1], state)) {
            count++
        }
    }

    return count
}

let state = JSON.parse(JSON.stringify(nums))
let prevState
do {
    prevState = JSON.parse(JSON.stringify(state))
    for (let i = 0; i < state.length; i++) {
        for (let j = 0; j < state[i].length; j++) {
            let visible = countVisible(i, j, prevState)

            if (prevState[i][j] === 'L' && !visible) {
                state[i][j] = '#'
            } else if (prevState[i][j] === '#' && visible >= 5) {
                state[i][j] = 'L'
            }
        }
    }
} while(!equal(state, prevState));

console.log(
    state.reduce((acc, row) => {
        return acc + row.reduce((acc, cell) => cell === '#' ? acc + 1 : acc, 0)
    }, 0)
)