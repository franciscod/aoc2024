from lib import *
# sys.setrecursionlimit(2999)

lines = inputlines()
rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
printmp(mp, rows, cols)

s = 0
for l in lines:
    s += len(l)

start = list(rmp["S"])[0]
end = list(rmp["E"])[0]
mp[end] = None

more = [(start, (0, 1), 0)]

def third(p):
    a, b, c = p
    return c

minc = {}
while more:
    more = list(sorted(more, key=third))
    (p, d, s), *more = more
    k = p, d
    mc = minc.get(k)
    if mc is not None and mc < s:
        continue
    minc[k] = s
    # print(k, s)
    if p == end:
        print("END", end)
        print(s)
        break
    py, px = p
    dy, dx = d
    ny, nx = py + dy, px + dx
    n = ny, nx
    nc = mp.get(n)
    # print(n, nc)
    if nc is None:
        more += [(n, d, s+1)]
    more += [(p, (-dx, dy), s+1000)]
    more += [(p, (dx, -dy), s+1000)]

print("?")
print(s)
