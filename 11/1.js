const fs = require('fs')

const nums = fs.readFileSync('./data', 'utf8').split("\n").map(r => r.split(''))
const rowMaxIndex = nums.length - 1
const colMaxIndex = nums[0].length - 1

const equal = (arr1, arr2) => {
    for (let i = 0; i < arr1.length; i++) {
        for (let j = 0; j < arr1[i].length; j++) {
            if (arr1[i][j] !== arr2[i][j]) {
                return false
            }
        }
    }
    return true
}

countNeighbours = (i, j, state) => {
    const maxRow = state.length - 1
    const maxCol = state[0].length - 1

    if (i > maxRow) {
        console.log('i > maxRow')
        process.exit(1)
    }

    if (j > maxCol) {
        console.log('j > maxCol')
        process.exit(1)
    }

    let neighbourIndexes = [
        i > 0 && j > 0 ? [i-1, j-1] : false,
        i > 0 ? [i-1, j  ] : false,
        i > 0 && j < maxCol  ? [i-1, j+1] : false,

        j > 0 ? [i, j-1] : false,
        // [i, j],
        j < maxCol ? [i, j+1] : false,

        i < maxRow && j > 0 ? [i+1, j-1] : false,
        i < maxRow ? [i+1, j  ] : false,
        i < maxRow && j < maxCol ? [i+1, j+1] : false,
    ]

    const neighbours = neighbourIndexes.reduce((acc, neighbour) => {
        if (!neighbour || neighbour[0] === false || neighbour[1] === false) {
            return acc
        }
        if (state[neighbour[0]][neighbour[1]] === '#') {
            return acc + 1
        }
        return acc
    }, 0)

    return neighbours
}


let state = JSON.parse(JSON.stringify(nums))
let prevState
do {
    prevState = JSON.parse(JSON.stringify(state))
    for (let i = 0; i < state.length; i++) {
        for (let j = 0; j < state[i].length; j++) {
            let neighbours = countNeighbours(i, j, prevState)

            if (prevState[i][j] === 'L' && !neighbours) {
                state[i][j] = '#'
            } else if (prevState[i][j] === '#' && neighbours >= 4) {
                state[i][j] = 'L'
            }
        }
    }
    // console.log(state.map(r => r.join('')).join("\n"))
    // console.log('')
} while(!equal(state, prevState));

console.log(
    state.reduce((acc, row) => {
        return acc + row.reduce((acc, cell) => cell === '#' ? acc + 1 : acc, 0)
    }, 0)
)