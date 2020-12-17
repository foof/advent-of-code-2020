from itertools import product

alive = set()

with open('./data') as f:
    for row, line in enumerate(f):
        for col, char in enumerate(line.strip()):
            if char == '#':
                alive.add((row, col, 0))

offsets = list([-1, 0, 1] for _ in range(3))
offsets = list(os for os in product(*offsets) if os != (0, 0, 0))

for r in range(6):
    print('Starting round %d' % r)
    new_alive = set()
    for i in range(min(a for a,_,_ in alive) - 1, max(a for a,_,_ in alive) + 2):
        for j in range(min(b for _,b,_ in alive) - 1, max(b for _,b,_ in alive) + 2):
            for k in range(-r - 1, r + 2):
                nbs = 0
                for os in offsets:
                    if (i+os[0],j+os[1],k+os[2]) in alive:
                        nbs += 1
                is_alive = (i,j,k) in alive
                if (is_alive and nbs in (2,3)) or (not is_alive and nbs == 3):
                    new_alive.add((i,j,k))
    alive = new_alive

print('Final: %d' % len(alive))