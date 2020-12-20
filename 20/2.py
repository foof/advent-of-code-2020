import re
import math

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

def get_all_tile_orientations(tiles):
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

tile_orientations = get_all_tile_orientations(tiles)

# Assumes the corners only have two possible neighbours
def corners_and_neighbours():
    corners = []
    neighbours = {}
    for t1_id in tiles:
        neighbours[t1_id] = []
        t1_o = tiles[t1_id]
        other_tile_ids = [t2_id for t2_id in tile_orientations if t2_id != t1_id]
        for t2_id in other_tile_ids:
            for t2_o in tile_orientations[t2_id]:
                if match_horizontal(t1_o, t2_o) or match_horizontal(t2_o, t1_o) or match_vertical(t1_o, t2_o) or match_vertical(t2_o, t1_o):
                    neighbours[t1_id].append(t2_id)
        if len(neighbours[t1_id]) == 2:
            corners.append(t1_id)

    return corners, neighbours


# Create square with empty cells
square_size = int(math.sqrt(len(tiles)))
def get_blank_puzzle(size):
    puzzle = []
    for _ in range(size):
        puzzle.append([None for _ in range(size)])
    return puzzle
puzzle = get_blank_puzzle(square_size)

# Get one corner piece and it's neighbours
corners, neighbours = corners_and_neighbours()
corner_id = corners[0]
used_ids = [corner_id, neighbours[corner_id][0], neighbours[corner_id][1]]
puzzle[0][0] = corner_id
puzzle[0][1] = neighbours[corner_id][0]
puzzle[1][0] = neighbours[corner_id][1]

count = 0
while len(used_ids) < len(tiles):
    count += 1
    for row_id in range(0, len(puzzle)):
        for col_id in range(0, len(puzzle)):
            if puzzle[row_id][col_id]:
                continue
            adjacent_ids = []
            if row_id != 0:
                adjacent_ids.append(puzzle[row_id-1][col_id])
            if col_id != 0:
                adjacent_ids.append(puzzle[row_id][col_id-1])
            adjacent_ids = [adjacent_id for adjacent_id in adjacent_ids if adjacent_id is not None]
            
            if len(adjacent_ids) == 0:
                # No adjacent ids
                continue

            if row_id == 0 and len(adjacent_ids) == 1 and not puzzle[1][col_id-1]:
                continue

            if col_id == 0 and len(adjacent_ids) == 1 and not puzzle[row_id-1][1]:
                continue

            if len(adjacent_ids) == 1 and row_id != 0 and col_id != 0:
                # require at least two adjacent ids for tiles that are not at the edges
                continue

            n_candidates = [n for n in neighbours[adjacent_ids[0]] if n not in used_ids]
            if len(adjacent_ids) > 1:
                for a_id in adjacent_ids[1:]:
                    n_candidates = [n for n in neighbours[a_id] if n not in used_ids and n in n_candidates]

            if len(n_candidates) == 1:
                puzzle[row_id][col_id] = n_candidates[0]
                used_ids.append(n_candidates[0])

tile_id = puzzle[0][0]

def get_solved_puzzle(start_tile):
    new_puzzle = get_blank_puzzle(square_size)
    new_puzzle[0][0] = start_tile
    for row_id in range(0, square_size):
        for col_id in range(0, square_size):
            if row_id == 0 and col_id == 0:
                continue
            for t2_o in tile_orientations[puzzle[row_id][col_id]]:
                if col_id == 0:
                    if match_vertical(new_puzzle[row_id-1][col_id], t2_o):
                        new_puzzle[row_id][col_id] = t2_o
                        break
                else:
                    if match_horizontal(new_puzzle[row_id][col_id-1], t2_o):
                        new_puzzle[row_id][col_id] = t2_o
                        break
            if not new_puzzle[row_id][col_id]:
                return False
    return new_puzzle


for t_o in tile_orientations[tile_id]:
    solved_puzzle = get_solved_puzzle(t_o)
    if solved_puzzle:
        break

tile_size = 10
image = [[] for _ in range(square_size * tile_size)]
for row_id in range(0, square_size):
    for col_id in range(0, square_size):
        tile = solved_puzzle[row_id][col_id]
        for rid, row in enumerate(tile):
            if rid == 0:
                continue
            if rid == len(tile)-1:
                continue
            for cid, char in enumerate(row):
                if cid == 0 :
                    continue
                if cid == len(row)-1:
                    continue
                image[(row_id*tile_size) + rid].append(char)


def flipimage(image):
    return list(reversed(image))

def rotateimage(tile):
    # rotates tile counter-clockwise 90 degrees
    tile_size = len(tile)
    new_tile = [[] for _ in tile]
    for row in tile:
        for j, cell in enumerate(row):
            new_tile[tile_size-j-1].append(cell)

    return new_tile
    
def all_image_orientations(image):
    res = []
    res.append(image)
    for i in range(0, 3):
        res.append(rotateimage(res[i]))
    res.append(flipimage(res[0]))
    for i in range(4, 7):
        res.append(rotateimage(res[i]))
    return res

image = [row for row in image if len(row) > 0]

image_orientations = all_image_orientations(image)

seamonster = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']
seamonster_deltas = []
seamonster_len = 20
seamonster_height = 3
for rid, row in enumerate(seamonster):
    for cid, char in enumerate(row):
        if char == '#':
            seamonster_deltas.append((rid, cid))

def find_seamonster(image):
    matches = []
    for rid in range(0, len(image[0])-seamonster_height):
        for cid in range(0, len(image)-seamonster_len):
            matching_deltas = []
            for d in seamonster_deltas:
                if image[rid+d[0]][cid+d[1]] == '#':
                    matching_deltas.append((rid+d[0], cid+d[1]))
            if len(matching_deltas) == len(seamonster_deltas):
                matches.append(matching_deltas)
    return matches

for i, i_o in enumerate(image_orientations):
    seamonster_matches = find_seamonster(i_o)
    if seamonster_matches:
        for coord_set in seamonster_matches:
            for coord in coord_set:
                i_o[coord[0]][coord[1]] = '.'
        ans = 0
        for row in i_o:
            for c in row:
                if c == '#':
                    ans += 1
        print(ans)
