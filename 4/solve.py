import re
import fileinput

ts = 0
en = True
mp = {}
cols = 0 

xs = set()
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

def readmp():
    for y, line in enumerate(fileinput.input()):
        line = line.strip()
        rows = y+1
        for x, c in enumerate(line):
            if c != '.':
                mp[y,x] = c

            cols = x+1

readmp()

for y, x in mp:
    c = mp[y,x]
    if c == 'X':
        xs.add((y, x))

print(f"xs: {len(xs)}")

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
for p in xs:
    for d in d8:
        k += findnmp(p, d, "MAS")

print(k)
