from lib import *
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

cs = set()
ns = defaultdict(set)
s = 0
for l in lines:
    a, b = l.split('-')
    cs.add((a, b))
    cs.add((b, a))
    ns[a].add(b)
    ns[b].add(a)
    s += len(l)

tics = set()
for p in ns:
    if p.startswith('t'):
        for q in ns[p]:
            for r in ns[p]:
                if q == r: continue
                if (r, q) in cs:
                    tics.add(tuple(sorted((p, q, r))))


print("?")
print(len(tics))
