
valid = []
other = []

with open('./data', 'r') as f:
    field_intervals, _, nearby_tickets = f.read().split("\n\n")
    for line in field_intervals.split("\n"):
        key, intervals = line.split(': ')
        for interval in intervals.split(' or '):
            f, t = interval.split('-')
            valid += [x for x in range(int(f), int(t) + 1)]
    for line in nearby_tickets.split("\n"):
        if line == 'nearby tickets:':
            continue
        other = other + [int(x) for x in line.split(',')]

diff = [i for i in other if i not in valid]

print(sum(diff))
