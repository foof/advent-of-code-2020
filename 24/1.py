
with open('./data') as f:
    tile_directions = []
    for line in f.read().split("\n"):
        d = []
        while len(line):
            if line[0] in 'ew':
                d.append(line[0])
                line = line[1:]
            else:
                d.append(line[0:2])
                line = line[2:]
        tile_directions.append(d)

odd_deltas = {}
odd_deltas['e'] = (0, 1)
odd_deltas['w'] = (0, -1)
odd_deltas['ne'] = (-1, 1)
odd_deltas['nw'] = (-1, 0)
odd_deltas['se'] = (1, 1)
odd_deltas['sw'] = (1, 0)

even_deltas = {}
even_deltas['e'] = (0, 1)
even_deltas['w'] = (0, -1)
even_deltas['ne'] = (-1, 0)
even_deltas['nw'] = (-1, -1)
even_deltas['se'] = (1, 0)
even_deltas['sw'] = (1, -1)

grid = [[] for _ in range(100)]
for row in grid:
    for _ in range(100):
        row.append(False)

for dirs in tile_directions:
    r, c = 40, 40
    for dir in dirs:
        deltas = even_deltas if r % 2 == 0 else odd_deltas
        r += deltas[dir][0]
        c += deltas[dir][1]
    grid[r][c] = not grid[r][c]

ans = 0
for row in grid:
    for cell in row:
        if cell:
            ans += 1
print(ans)
