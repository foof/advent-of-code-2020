const fs = require('fs')

const map = fs.readFileSync('./data', 'utf8').split("\n").map(row => row.split(''))
const [height, width] = [map.length, map[0].length]
const slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

const result = slopes.reduce((acc, slope) => {
    const [dx, dy] = slope
    const pos = { x: 0, y: 0 }
    let trees = 0
    while (pos.y + dy <= height - 1) {
        pos.x = (pos.x + dx) % width
        pos.y += dy
        if (map[pos.y][pos.x] === '#') {
            trees++
        }
    };
    return acc ? acc * trees : trees
}, 0)



console.log(result)