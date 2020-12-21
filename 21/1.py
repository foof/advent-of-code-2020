
possible = {}
all_ingredients = []

with open('./data') as f:
    for line in f.read().split("\n"):
        ingredients, allergens = line[0:-1].split(' (contains ')
        allergens = allergens.split(', ')
        ingredients = ingredients.split(' ')
        all_ingredients = all_ingredients + ingredients
        for a in allergens:
            if a not in possible.keys():
                possible[a] = set(ingredients)
            else:
                possible[a] = possible[a].intersection(ingredients)

can_have_allergens = set([i for p in possible.values() for i in p])

print(len([i for i in all_ingredients if i not in can_have_allergens]))