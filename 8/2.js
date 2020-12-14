const fs = require('fs')

const instructions = fs.readFileSync('./data', 'utf8').split("\n").map(inst => inst.split(' '))
const jmps = instructions.map((inst, idx) => inst[0] === 'jmp' ? idx : 0)
const nops = instructions.map((inst, idx) => inst[0] === 'nop' ? idx : 0)

const runProgram = (instructions) => {
    let pCount = 0
    let accumulator = 0
    const visitedInstructions = new Set()

    while (pCount < instructions.length) {
        if (visitedInstructions.has(pCount)) {
            return [false, accumulator]
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

    return [true, accumulator]
}

jmps.forEach(idx => {
    let instructionsCopy = instructions.slice(0)
    instructionsCopy[idx] = ['nop', instructionsCopy[idx][1]]
    let [result, acc] = runProgram(instructionsCopy)
    if (result) {
        console.log(acc)
    }
})

nops.forEach(idx => {
    let instructionsCopy = instructions.slice(0)
    instructionsCopy[idx] = ['jmp', instructionsCopy[idx][1]]
    let [result, acc] = runProgram(instructionsCopy)
    if (result) {
        console.log(acc)
    }
})