
lines = list([l.strip() for l in open('./data').readlines()])
rules = {}
dp = {}

def match_list(line, start, end, rules):
    if start==end and not rules:
        # End of string and no more rules
        return True
    if start==end and rules:
        # End of string but there are more rules
        return False
    if not rules:
        # Not end of string but there are no more rules to check
        return False

    ret = False
    for i in range(start+1, end+1):
        if match(line, start, i, rules[0]) and match_list(line, i, end, rules[1:]):
            ret = True

    return ret

def match(line, start, end, rule):
    key = (start, end, rule)
    if key in dp:
        return dp[key]

    result = False
    if type(rules[rule]) is str:
        result = line[start:end] == rules[rule]
    else:
        for option in rules[rule]:
            if match_list(line, start, end, option):
                result = True

    dp[key] = result
    return result

def solve():
    rules['8'] = [x.split(' ') for x in '42 | 42 8'.split(' | ')]
    rules['11'] = [x.split(' ') for x in  '42 31 | 42 11 31'.split(' | ')]

    ans = 0
    for line in lines:
        if ':' in line:
            key, rule = line.split(': ')
                
            if '"' in rule:
                rules[key] = eval(rule)
            elif key not in rules:
                options = rule.split(' | ')
                rules[key] = [x.split(' ') for x in options]
        elif line:
            dp.clear()
            if match(line, 0, len(line), '0'):
                ans += 1
    return ans

print(solve())
