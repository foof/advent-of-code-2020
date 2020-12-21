
possible_map = {}
all_ingredients = []

with open('./data') as f:
    for line in f.read().split("\n"):
        ingredients, allergens = line[:-1].split(' (contains ')
        allergens = allergens.split(', ')
        ingredients = set(ingredients.split(' '))
        all_ingredients += list(ingredients)
        for a in allergens:
            if a not in possible_map.keys():
                possible_map[a] = ingredients
            else:
                possible_map[a] &= ingredients

can_have_allergens = set([i for p in possible_map.values() for i in p])

print(len([i for i in all_ingredients if i not in can_have_allergens]))
