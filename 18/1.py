import re

def compute(expr):
    while True:
        match = re.search(r'\d+ [+*]{1} \d+', expr)
        if not match:
            break
        expr = expr.replace(match.group(0), str(eval(match.group(0))), 1)
    return eval(expr)

def solve(expr):
    while True:
        match = re.search(r'\([^()]+\)', expr)
        if not match:
            break
        expr = expr.replace(match.group(0), str(compute(match.group(0)[1:-1])))
    return compute(expr)

with open('./data', 'r') as f:
    print(sum([solve(expr) for expr in f]))
