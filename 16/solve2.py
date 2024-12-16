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

more = [(start, (0, 1), 0, [start])]

def third(p):
    a, b, c, *_ = p
    return c

goodtiles = set()
best = None
minc = {}
mincp = {}
while more:
    more = list(sorted(more, key=third))
    (p, d, s, path), *more = more
    if best is not None and s > best:
        break
    k = p, d
    mc = minc.get(k)
    if mc is not None and mc < s:
        continue
    minc[k] = s
    mincp[p] = s
    # print(k, s)
    if p == end:
        best = s
        print("END", end)
        for p  in path:
            goodtiles.add(p)
        print(s)
        continue
    py, px = p
    dy, dx = d
    ny, nx = py + dy, px + dx
    n = ny, nx
    nc = mp.get(n)
    # print(n, nc)
    if nc is None:
        more += [(n, d, s+1, path + [n])]
    more += [(p, (-dx, dy), s+1000, path)]
    more += [(p, (dx, -dy), s+1000, path)]

# k = 0
# more = [(end, best)]
# goodtiles = set()
# while more:
#     (p,s), *more = more
#     goodtiles.add(p)
#     print(p, s)
#     for n in neighs(p, nd4a):
#         nc = mincp.get(n)
#         print(p, n, nc)
#         if nc == s-1:
#             more += [(n, s-1)]
#         if nc == s-1001:
#             more += [(n, s-1001)]
# 
# for p in goodtiles:
#     mp[p] = "O"
# 
# printmp(mp, rows, cols)
print(len(goodtiles))

