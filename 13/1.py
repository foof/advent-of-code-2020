with open('./data', 'r') as f:
    arrival, buses = f.read().splitlines()
    arrival = int(arrival)
    
buses = [int(b) for b in buses.split(',') if b != 'x']

best = None
for bus in buses:
    wait = bus - arrival%bus
    if not best or wait < best[1]:
        best = (bus, wait)

print(best[0]*best[1])
