from lib import *
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

mp = {}
# rows, cols, skip = 7, 7, 12
rows, cols, skip = 71, 71, 2986
for i, l in enumerate(lines):
    if i >= skip:
        continue
    x, y = parseints(l, ',')
    mp[y,x] = '#'

print (lines[skip])


# printmp(mp, rows, cols)

start = 0, 0
end = (rows-1, cols-1)

more = [(start, 0, [start])]

cost = {}
def heur(tup):
    p, s, path = tup
    return -cost[p]

while more:
    # more = list(sorted(more, key=heur))
    (p, s, path), *more = more
    if p in cost:
        continue
    cost[p] = s
    mp[p] = 'O'
    # printmp(mp, rows, cols)
    # print(p, s, path)
    if p == end:
        print("END", end)
        print(s)
        exit(0)
        for p in path:
            goodtiles.add(p)
            
        print(s)
        continue
    for n in neighs(p, nd4a):
        if mp.get(n) == '#':
            continue
        if n in cost:
            continue
        if inbounds(p, start, (rows, cols)):
            more += [(n, s+1, path + [n])]

print("?")
print(s)
