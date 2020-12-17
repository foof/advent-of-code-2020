with open('./data', 'r') as f:
    _, buses = f.read().splitlines()
    
buses = [(int(b), int(-i) % int(b)) for i, b in enumerate(buses.split(',')) if b != 'x']
buses.sort(key=lambda bus: bus[1], reverse=True)

step, t = buses[0]
for b, mod in buses[1:]:
    while t % b != mod:
        t += step
    step *= b
print(t)
