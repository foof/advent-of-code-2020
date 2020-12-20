import re

tiles = {}
for tile_block in open('./data').read().split("\n\n"):
    tile_lines = tile_block.split("\n")
    tile_id = int(re.search(r'\d+', tile_lines[0])[0])
    tile = []
    for line in tile_lines[1:]:
        tile.append(list(line))
    tiles[tile_id] = tile

def rotate(tile):
    # rotates tile counter-clockwise 90 degrees
    tile_size = len(tile)
    new_tile = [[] for _ in tile]
    for row in tile:
        for j, cell in enumerate(row):
            new_tile[tile_size-j-1].append(cell)

    return new_tile

def flip(tile):
    return list(reversed(tile))

def get_all_orientations(tiles):
    res = {}
    for t in tiles:
        res[t] = []
        res[t].append(tiles[t])
        for i in range(0, 3):
            res[t].append(rotate(res[t][i]))
        res[t].append(flip(res[t][0]))
        for i in range(4, 7):
            res[t].append(rotate(res[t][i]))
    return res

def match_horizontal(left_tile, right_tile):
    for i in range(len(left_tile)):
        if left_tile[i][-1] != right_tile[i][0]:
            return False
    return True

def match_vertical(over_tile, under_tile):
    return over_tile[-1] == under_tile[0]

tile_orientations = get_all_orientations(tiles)

# Assumes the corners only have two possible neighbours
def part1():
    ans = 1
    for t1_id in tiles:
        possible_neighbours = 0
        t1_o = tiles[t1_id] # Doesn't matter which orientation t1 is since we compare with all orientations of t2
        other_tile_ids = [t2_id for t2_id in tile_orientations if t2_id != t1_id]
        for t2_id in other_tile_ids:
            # Check if the two tiles match in any direction and orientation
            for t2_o in tile_orientations[t2_id]:
                if match_horizontal(t1_o, t2_o) or match_horizontal(t2_o, t1_o) or match_vertical(t1_o, t2_o) or match_vertical(t2_o, t1_o):
                    possible_neighbours += 1
        if possible_neighbours == 2:
            # If there are only two possible neighbours, we know for sure this is a corner piece
            ans *= t1_id
    return ans

print(part1())
