from collections import defaultdict

fields = defaultdict(list)
valid = []
valid_tickets = []
my_ticket = []

with open('./data', 'r') as f:
    field_intervals, t, nearby_tickets = f.read().split("\n\n")

    # My ticket
    my_ticket = [int(x) for x in t.split("\n")[1].split(',')]

    # All valid values for each key
    for line in field_intervals.split("\n"):
        key, intervals = line.split(': ')
        for interval in intervals.split(' or '):
            f, t = interval.split('-')
            new_valid_fields = list(range(int(f), int(t) + 1))
            fields[key] += new_valid_fields
            valid += new_valid_fields

    # All valid tickets
    for line in nearby_tickets.split("\n"):
        if line == 'nearby tickets:':
            continue
        ticket = [int(x) for x in line.split(',') if int(x) in valid]
        if len(ticket) == len(fields):
            valid_tickets.append(ticket)

keys = list(fields.keys())
number_of_keys = range(len(keys))
possible_keys = defaultdict(list)

for i in number_of_keys:
    for key in keys:
        invalid = False
        for ticket in valid_tickets:
            if ticket[i] not in fields[key]:
                invalid = True
                break
        if not invalid:
            possible_keys[i].append(key)

solved = {}
while len(solved) < len(keys):
    for i in number_of_keys:
        if len(possible_keys[i]) == 0:
            continue
        if len(possible_keys[i]) == 1:
            solved[i] = possible_keys[i][0]
            for j in number_of_keys:
                possible_keys[j] = [key for key in possible_keys[j] if key != solved[i]]

departure_idx = [i for i in solved if solved[i].startswith('departure')]

ans = 1
for i in departure_idx:
    ans *= my_ticket[i]

print(ans)