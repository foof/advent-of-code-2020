import re

def compute(expr):
    while True:
        match = re.search(r'\d+ \+ \d+', expr)
        if not match:
            break
        expr = expr[:match.start()] + str(eval(match[0])) + expr[match.end():]
    return eval(expr)

def solve(expr):
    while True:
        match = re.search(r'\([^()]+\)', expr)
        if not match:
            break
        expr = expr.replace(match[0], str(compute(match[0][1:-1])))
    return compute(expr)

with open('./data', 'r') as f:
    print(sum([solve(expr) for expr in f]))
