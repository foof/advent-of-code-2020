const fs = require('fs')

const map = fs.readFileSync('./data', 'utf8').split("\n").map(row => row.split(''))
const [height, width] = [map.length, map[0].length]
const [dx, dy] = [3, 1]
const pos = { x: 0, y: 0 }
let trees = 0

while (pos.y + dy <= height - 1) {
    pos.x = (pos.x + dx) % width
    pos.y += dy
    if (map[pos.y][pos.x] === '#') {
        trees++
    }
};

console.log(trees)