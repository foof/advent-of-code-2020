import re

def compute(expr):
    match = re.search(r'\d+ (\+|\*) \d+', expr)
    while match:
        replacement = '%d' % eval(match.group(0))
        expr = expr.replace(match.group(0), replacement, 1)
        match = re.search(r'\d+ (\+|\*) \d+', expr)
    return int(expr)

def solve(expr):
    match = re.search(r'\([^\(\)]*\)', expr)
    while match:
        replacement = '%d' % compute(match.group(0)[1:-1])
        expr = expr.replace(match.group(0), replacement)
        match = re.search(r'\([^\(\)]*\)', expr)
    return compute(expr)

with open('./data', 'r') as f:
    print(sum([solve(expr) for expr in f]))
