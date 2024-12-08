import fileinput

from collections import defaultdict
from itertools import combinations

def pairs(s):
    return combinations(s, 2)

def inbounds(p, lb, ub):
    py, px = p
    ly, lx = lb
    uy, ux = ub

    return (ly <= py < uy) and (lx <= px < ux)

def readmp(lines):
    m = {}
    rm = defaultdict(set)
    for y, line in enumerate(lines):
        line = line.strip()
        rows = y+1
        for x, c in enumerate(line):
            cols = x+1
            if c == '.':
                continue
            m[y,x] = c
            rm[c].add((y, x))


    return rows, cols, m, rm


def printmp(m, rows, cols):
    for y in range(rows):
        for x in range(cols):
            print(m.get((y, x), '.'), end='')
        print()


def inputlines():
    lines = []
    for line in fileinput.input():
        line = line.strip()
        lines.append(line)
    return lines

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
