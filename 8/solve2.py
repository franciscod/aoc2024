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

        cy = ay
        cx = ax
        while True:
            antis.add((cy, cx))
            if not inbounds((cy, cx), (0, 0), (rows, cols)):
                break
            cy += dy
            cx += dx

        cy = by
        cx = bx
        while True:
            antis.add((cy, cx))
            if not inbounds((cy, cx), (0, 0), (rows, cols)):
                break
            cy -= dy
            cx -= dx

k = 0
for y, x in antis:
    if inbounds((y, x), (0, 0), (rows, cols)):
        m.setdefault((y, x),'#')
        k += 1

printmp(m, rows, cols)
print(k)
