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
line = lines[0]
print(line)

disk = []
for i, c in enumerate(line):
    n = int(c)
    fid = None
    if i % 2 == 0:
        fid = i//2
    for _ in range(n):
        disk.append(fid)

print(disk)

def defrag(disk):
    nd = []
    i = 0
    j = len(disk) - 1
    while i <= j:
        if disk[i] is not None:
            yield disk[i]
        else:
            while disk[j] is None:
                j -= 1
            yield disk[j]
            j -= 1
        i += 1


chk = list(defrag(disk))
print(chk)

s = 0
for i, n in enumerate(chk):
    s += i * n
print(s)

