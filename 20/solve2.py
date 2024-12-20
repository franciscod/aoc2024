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

savc = Counter()

goodcheats = set()
for i, p in enumerate(d2e):
    print(i, len(d2e))
    d1 = d2e[p]
    for c in range(1, 21):
        for cy in range(-20, 21):
            for cx in range(-20, 21):
                if abs(cy)+abs(cx) == c:
                    py, px = p
                    qy, qx = py + cy, px + cx
                    q = qy, qx

                    if q in d2e:
                        d2 = d2e[q]
                        sav = abs(d1 - d2) -c
                        if sav >= 100:
                            savc[sav]+=0.5
                            # print(sav)


# print(d2e[start])
# print(len(goodcheats))
print(int(savc.total()))
