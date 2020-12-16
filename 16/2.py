
fields = {}
valid = []
other = []
my_t = []

with open('./data', 'r') as f:
    one, my_t, nearby_t = f.read().split("\n\n")
    my_ticket = [int(x) for x in my_t.split("\n")[1].split(',')]
    for line in one.split("\n"):
        key, intervals = line.split(': ')
        fields[key] = []
        for interval in intervals.split(' or '):
            f, t = interval.split('-')
            for i in range(int(f), int(t) + 1):
                fields[key].append(int(i))
                valid.append(int(i))
    for line in nearby_t.split("\n"):
        if line == 'nearby tickets:':
            continue
        ticket_values = line.split(',')
        ticket = [int(x) for x in ticket_values if int(x) in valid]
        if len(ticket) == len(ticket_values):
            other.append(ticket)

keys = list(fields.keys())
field_map = {}
possible_keys = {}

for i in range(len(keys)):
    possible_keys[i] = []
    for key in keys:
        invalid = False
        for ticket in other:
            if ticket[i] not in fields[key]:
                invalid = True
                break
        if not invalid:
            possible_keys[i].append(key)

solved = {}
while len(solved) < len(keys):
    for i in range(len(keys)):
        to_delete = None
        if len(possible_keys[i]) == 0:
            continue
        if len(possible_keys[i]) == 1:
            to_delete = possible_keys[i][0]
            solved[i] = to_delete
        if not to_delete:
            continue
        for j in range(len(keys)):
            possible_keys[j] = [key for key in possible_keys[j] if key != to_delete]

ans = 1
for i in solved:
    if not solved[i].startswith('departure'):
        continue
    ans *= my_ticket[i]

print(ans)