from lib import *

lines = inputlines()

rows, cols, m, ants = readmp(lines)

print(rows, cols, ants)

freqs = set(ants)

antis = set()
for f in freqs:
    for a, b in pairs(ants[f]):
        ay, ax = a
        by, bx = b
        dy = ay - by
        dx = ax - bx

        c0y = ay + dy
        c0x = ax + dx
        c0 = (c0y, c0x)

        c1y = by - dy
        c1x = bx - dx
        c1 = (c1y, c1x)

        antis.add(c0)
        antis.add(c1)

k = 0
for y, x in antis:
    if inbounds((y, x), (0, 0), (rows, cols)):
        m.setdefault((y, x),'#')
        k += 1

printmp(m, rows, cols)
print(k)
