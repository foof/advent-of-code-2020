
possible = {}

with open('./data') as f:
    for line in f.read().split("\n"):
        ingredients, allergens = line[0:-1].split(' (contains ')
        ingredients = ingredients.split(' ')
        for a in allergens.split(', '):
            if a not in possible.keys():
                possible[a] = ingredients
            else:
                possible[a] = [i for i in ingredients if i in possible[a]]

final_map = {}
while final_map.keys() < possible.keys():
    for a in possible:
        if len(possible[a]) == 1:
            final_map[a] = possible[a][0]
            for a2 in possible:
                possible[a2] = [i for i in possible[a2] if i != final_map[a]]

ingredients = ','.join([final_map[k] for k in sorted(final_map.keys())])
print(ingredients)