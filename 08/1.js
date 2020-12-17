const fs = require('fs')

const instructions = fs.readFileSync('./data', 'utf8').split("\n").map(inst => inst.split(' '))

let pCount = 0
let accumulator = 0
const visitedInstructions = new Set()

while (pCount < instructions.length) {
    if (visitedInstructions.has(pCount)) {
        console.log('accumulator', accumulator)
        break
    }

    visitedInstructions.add(pCount)

    let [instruction, value] = instructions[pCount]
    switch (instruction) {
        case 'acc':
            accumulator += eval(value)
            pCount++
            break;

        case 'jmp':
            pCount += eval(value)
            break;

        case 'nop':
            pCount++
            break;
    }
}