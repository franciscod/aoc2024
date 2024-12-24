from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
g = iter(lines)

known = set()
vals = {}
ops = {}
deps = defaultdict(set)
unlocks = defaultdict(set)
pend = set()

for l in g:
    if l == "":
        break
    a, b = l.split(': ')
    vals[a] = int(b)
    known.add(a)

for l in g:
    ws = l.split()
    a, op, b, _, r = ws
    ops[r] = (op, a, b)
    known.add(a)
    known.add(b)
    known.add(r)
    pending = False
    if a not in vals:
        deps[r].add(a)
        unlocks[a].add(r)
        pending = True
    if b not in vals:
        deps[r].add(b)
        unlocks[b].add(r)
        pending = True

    if pending:
        pend.add(r)

def ss(k):
    print("ss", k)
    if k in vals:
        return

    for d in deps[k]:
        ss(d)

    op, ka, kb = ops[k]
    a = vals[ka]
    b = vals[kb]

    OPMAP = {
            'AND': (lambda a, b: a&b),
            'OR': (lambda a, b: a|b),
            'XOR': (lambda a, b: a^b),
            }

    vals[k] = OPMAP[op](a, b)

def step():
    for k in known:
        if k.startswith('z'):
            ss(k)

    rs = ((k,v) for k, v in vals.items() if k.startswith('z'))
    rs = list(sorted(rs))
    pprint(rs)

    return int(''.join(reversed(list(str(v) for k, v in rs))), 2)

# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

print(step())
