buses = [13,'x','x',41,'x','x','x','x','x','x','x','x','x',997,'x','x','x','x','x','x','x',23,'x','x','x','x','x','x','x','x','x','x',19,'x','x','x','x','x','x','x','x','x',29,'x',619,'x','x','x','x','x',37,'x','x','x','x','x','x','x','x','x','x',17]

mods = {bus: -i % bus for i, bus in enumerate(buses) if bus != "x"}
bus_ids = list(reversed(sorted(mods)))
val = mods[bus_ids[0]]
step = bus_ids[0]
for bus_id in bus_ids[1:]:
    while val % bus_id != mods[bus_id]:
        val += step
    step *= bus_id
print(val)
