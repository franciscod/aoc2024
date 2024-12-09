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

disk = []
for i, c in enumerate(line):
    n = int(c)
    fid = None
    if i % 2 == 0:
        fid = i//2

    disk.append((fid, n))

# print(disk)

def printdisk(disk):
    for f, s in disk:
        if f is None:
            f = '.'
        print(str(f) * s, end='')
    print()

def defrag(disk):
    nd = []
    i = len(disk) - 1
    while i > 0:
        fid, si = disk[i]
        if fid is not None:
            #print("trying", fid, si)
            moved = False
            for j in range(i):
                fjd, sj = disk[j]
                if fjd is not None:
                    continue
                if si <= sj:
                    # print("- moving!")
                    disk[j:j+1] = [(fid, si), (None, sj - si)]
                    disk[i+1] = (None, si)
                    # printdisk(disk)
                    moved = True
                    break
                if moved:
                    break
            else:
                pass#print("- staying.")
        i -= 1

    return (disk)

chk = list(defrag(disk))

def raw(disk):
    for f, s in disk:
        for _ in range(s):
            yield f

s = 0
for i, n in enumerate(raw(disk)):
    if n is None:
        continue
    s += i * n
print(s)

