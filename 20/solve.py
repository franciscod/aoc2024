from lib import *
sys.setrecursionlimit(9999)

lines = inputlines()
rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

start = list(rmp['S'])[0]
end = list(rmp['E'])[0]

d2e = dict()
more = [(end, 0)]
while more:
    (p, d), *more = more
    if p in d2e:
        continue
    # print("exp", p, d)
    d2e[p] = d
    for (ny, nx), (dy, dx) in neighsd(p, nd4a):
        n1 = (ny, nx)
        if mp.get(n1) != '#':
            more.append((n1, d+1))

goodcheats = set()
for p in d2e:
    py, px = p
    d1 = d2e[p]
    for n1, d in neighsd(p, nd4a):
        dy, dx = d
        n1y, n1x = n1
        n2y, n2x = n1y + dy, n1x + dx
        n2 = n2y, n2x
        if n2 in d2e:
            d2 = d2e[n2]
            sav = abs(d1 - d2) -2
            # print(n1, sav)
            if sav >= 100:
                goodcheats.add(n1)

print(d2e[start])
print(len(goodcheats))
