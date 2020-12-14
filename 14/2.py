import itertools

data = open('./data', 'r').read().splitlines()

mem = {}
mask = None
zeromask = 0
onemask = 1
for line in data:
    op,val = line.split(' = ')

    if (op == 'mask'):
        mask = val
        zeromask = eval('0b{}'.format(val.replace('1', 'X').replace('X','1')))
        onemask = eval('0b{}'.format(val.replace('0', 'X').replace('X','0')))

    if (op[:3] == 'mem'):
        val = int(val)
        address = int(op[4:].rstrip(']'))
        masked_address = address | onemask

        xs = [idx for idx,c in enumerate(mask[::-1]) if c == 'X'] # Get the indices of all Xs
        pairs = [[0, 1] for i in range(len(xs))] # Generate x number of [0,1] pairs where x is the amount of xs in the mask
        bit_combos = [e for e in itertools.product(*pairs)] # Cartesian product of all pairs
        for bit_combo in bit_combos:
            new_address = masked_address
            one_address_mask = 0b00000000000000000000000000000000000
            zero_address_mask = 0b00000000000000000000000000000000000

            for j,bit in enumerate(bit_combo):
                if bit == 1:
                    one_address_mask |= 2**xs[j]
                else:
                    zero_address_mask |= 2**xs[j]

            zero_address_mask = ~zero_address_mask
            new_address = (new_address | one_address_mask) & zero_address_mask
            mem[new_address] = val

print(sum(mem.values()))