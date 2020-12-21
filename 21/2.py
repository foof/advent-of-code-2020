
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

final_solution = {}
while final_solution.keys() < possible.keys():
    for a in possible:
        if len(possible[a]) == 1:
            final_solution[a] = possible[a][0]
            for a2 in possible:
                possible[a2] = [i for i in possible[a2] if i != final_solution[a]]

ingredients = ','.join([final_solution[k] for k in sorted(final_solution.keys())])
print(ingredients)