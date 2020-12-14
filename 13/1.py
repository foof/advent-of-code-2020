arrival = 1000390
buses = [13,'x','x',41,'x','x','x','x','x','x','x','x','x',997,'x','x','x','x','x','x','x',23,'x','x','x','x','x','x','x','x','x','x',19,'x','x','x','x','x','x','x','x','x',29,'x',619,'x','x','x','x','x',37,'x','x','x','x','x','x','x','x','x','x',17]
buses = [int(x) for x in buses if x != 'x']

best = None
for bus in buses:
    wait = bus - arrival%bus
    if not best or wait < best[1]:
        best = (bus, wait)

print(best[0]*best[1])
