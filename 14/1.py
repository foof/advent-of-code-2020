
data = open('./data', 'r').read().splitlines()

mem = {}
zeromask = None
onemask = None
for line in data:
    op,val = line.split(' = ')

    if (op == 'mask'):
        zeromask = eval('0b{}'.format(val.replace('1', 'X').replace('X','1')))
        onemask = eval('0b{}'.format(val.replace('0', 'X').replace('X','0')))

    if (op[:3] == 'mem'):
        address = int(op[4:].rstrip(']'))
        val = (int(val) | onemask) & zeromask
        mem[address] = val

print(sum(mem.values()))