from lib import *

ts = 0
en = True
mp = {}

aas = set()

rows, cols, mp, _ = readmp(inputlines())

for y, x in mp:
    c = mp[y,x]
    if c == 'A':
        aas.add((y, x))

def findnmp(p, d, rest):
    py, px = p
    dy, dx = d
    n = (py+dy, px+dx)

    h, *t = rest
    if mp.get(n, '.') != h:
        return 0
    if not t:
        return 1

    return findnmp(n, d, t)

k = 0
for p in aas:
    pk = 0
    for d in nd4d:
        od = dopp(d)
        pk += findnmp(p, d, "M") * findnmp(p, od, "S")
    if pk == 2:
        k += 1
        print(p, pk, k)

print(k)
# printmp(mp, rows, cols)
