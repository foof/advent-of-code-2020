data = open('./data', 'r').read().split(',')
data = [int(x) for x in data]

mem = {}
prev = data[-1]

# Initialize
for t, starting_number in enumerate(data):
    mem[starting_number] = t

# Start game
for t in range(len(data), 2020):
    if prev in mem:
        last_t = mem[prev]

        if last_t == t - 1:
            speak = 0
        else:
            speak = (t - 1) - mem[prev]
            mem[prev] = t - 1
    else:
        speak = 0
        mem[prev] = t - 1

    prev = speak

print(prev)