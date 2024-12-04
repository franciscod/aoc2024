import re
import fileinput

ts = 0
en = True
mp = {}

aas = set()
d8 = (
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0, -1),
    ( 0,  1),
    ( 1, -1),
    ( 1,  0),
    ( 1,  1),
)

d4d = (
    (-1, -1),
    (-1,  1),
    ( 1, -1),
    ( 1,  1),
)

def opp(d):
    dy, dx = d
    return -dy, -dx

cols = 0
rows = 0
def readmp():
    global rows, cols
    for y, line in enumerate(fileinput.input()):
        line = line.strip()
        rows = y+1
        for x, c in enumerate(line):
            if c != '.':
                mp[y,x] = c

            cols = x+1

readmp()

def printmp():
    for y in range(rows):
        for x in range(cols):
            c = mp.get((y,x), '.')
            print(c, end='')
        print()

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
    for d in d4d:
        od = opp(d)
        pk += findnmp(p, d, "M") * findnmp(p, od, "S")
    if pk == 2:
        k += 1
        print(p, pk, k)

print(k)
# printmp()
