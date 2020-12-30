
from copy import deepcopy

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

def count_black(grid):
    ans = 0
    for row in grid:
        for cell in row:
            if cell:
                ans += 1
    return ans

grid_size = 140
grid = [[] for _ in range(grid_size)]
for row in grid:
    for _ in range(grid_size):
        row.append(False)

for dirs in tile_directions:
    r, c = grid_size//2, grid_size//2
    for dir in dirs:
        deltas = even_deltas if r % 2 == 0 else odd_deltas
        r += deltas[dir][0]
        c += deltas[dir][1]
    grid[r][c] = not grid[r][c]


def part2(grid):
    for day in range(100):
        new_grid = deepcopy(grid)
        for r, row in enumerate(grid):
            deltas = even_deltas if r % 2 == 0 else odd_deltas
            for c, col in enumerate(row):
                black_neighbours = 0
                for delta in deltas.values():
                    n_r = r+delta[0]
                    n_c = c+delta[1]
                    if n_r < 0 or n_c < 0 or n_r >= grid_size or n_c >= grid_size:
                        # Out of bounds
                        continue
                    if grid[n_r][n_c]:
                        black_neighbours += 1
                if col and not 1<=black_neighbours<=2: # Black
                    new_grid[r][c] = False
                elif not col and black_neighbours == 2: # White
                    new_grid[r][c] = True
        grid = new_grid
    return count_black(grid)

print(part2(grid))
