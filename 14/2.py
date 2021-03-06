import itertools

data = open('./data', 'r').read().splitlines()

mem = {}
mask = None
onemask = 1
for line in data:
    op,val = line.split(' = ')

    if (op == 'mask'):
        mask = val
        onemask = eval('0b{}'.format(val.replace('0', 'X').replace('X','0')))

    if (op.startswith('mem')):
        masked_address = int(op[4:-1]) | onemask

        xs = [idx for idx,c in enumerate(mask[::-1]) if c == 'X'] # Get the indices of all Xs
        pairs = [[0, 1] for i in range(len(xs))] # Generate x number of [0,1] pairs where x is the number of Xs in the mask
        bit_combos = [e for e in itertools.product(*pairs)] # Cartesian product of all pairs
        for bit_combo in bit_combos:
            one_address_mask = 0
            zero_address_mask = 0

            for j,bit in enumerate(bit_combo):
                if bit == 1:
                    one_address_mask |= 2**xs[j]
                else:
                    zero_address_mask |= 2**xs[j]

            new_address = (masked_address | one_address_mask) & ~zero_address_mask
            mem[new_address] = int(val)

print(sum(mem.values()))
