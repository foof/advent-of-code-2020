
valid = []
other = []

with open('./data', 'r') as f:
    one, my_t, nearby_t = f.read().split("\n\n")
    for line in one.split("\n"):
        key, intervals = line.split(': ')
        for interval in intervals.split(' or '):
            f, t = interval.split('-')
            for i in range(int(f), int(t) + 1):
                valid.append(int(i))
    for line in nearby_t.split("\n"):
        if line == 'nearby tickets:':
            continue
        for x in line.split(','):
            other.append(int(x))

diff = [i for i in other if i not in valid]

print(sum(diff))
