
possible_map = {}

with open('./data') as f:
    for line in f.read().split("\n"):
        ingredients, allergens = line[:-1].split(' (contains ')
        ingredients = ingredients.split(' ')
        for a in allergens.split(', '):
            if a not in possible_map.keys():
                possible_map[a] = ingredients
            else:
                possible_map[a] = [i for i in ingredients if i in possible_map[a]]

final_map = {}
while len(final_map) < len(possible_map):
    for a in possible_map:
        if len(possible_map[a]) == 1:
            final_map[a] = possible_map[a][0]
            for a2 in possible_map:
                possible_map[a2] = [i for i in possible_map[a2] if i != final_map[a]]

print(','.join([final_map[k] for k in sorted(final_map.keys())]))
