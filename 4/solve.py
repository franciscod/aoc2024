from lib import *

ts = 0
en = True
mp = {}
cols = 0 

xs = set()

rows, cols, mp, _ = readmp(inputlines())

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
    for d in nd8:
        k += findnmp(p, d, "MAS")

print(k)
