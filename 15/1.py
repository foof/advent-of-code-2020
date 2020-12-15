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
        speak = (t - 1) - mem[prev]
    else:
        speak = 0

    mem[prev] = t - 1
    prev = speak

print(prev)