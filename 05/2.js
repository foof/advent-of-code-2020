const fs = require('fs')

const seats = fs.readFileSync('./data', 'utf8').split("\n").map(row => row.split(''))

const result = seats.map(data => {
    const rowData = data.splice(0, 7)
    const colData  = data

    const row = rowData.reduce((acc, letter) => {
        if (letter === 'F') {
            acc.to -= Math.ceil((acc.to - acc.from) / 2)
        }
        if (letter === 'B') {
            acc.from += Math.ceil((acc.to - acc.from) / 2)
        }
        return acc
    }, { from: 0, to: 127})

    const col = colData.reduce((acc, letter) => {
        if (letter === 'L') {
            acc.to -= Math.ceil((acc.to - acc.from) / 2)
        }
        if (letter === 'R') {
            acc.from += Math.ceil((acc.to - acc.from) / 2)
        }
        return acc
    }, { from: 0, to: 7})

    return row.from * 8 + col.from
}).sort((a, b) => a - b).reduce((acc, seat, idx, source) => {
    if (idx === source.length - 1) {
        return acc
    }
    if (source[idx - 1] !== seat - 1) {
        return seat - 1
    }
    return acc
})

console.log(result)