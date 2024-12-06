import fileinput
from collections import defaultdict

import re
import fileinput

ts = 0
en = True
mp = {}
cols = 0 
rows = 0

d = None
guard = None
walls = set()

def readmp():
    global guard
    global d
    global rows
    global cols

    for y, line in enumerate(fileinput.input()):
        line = line.strip()
        rows = y+1
        for x, c in enumerate(line):
            if c == '#':
                walls.add((y,x))
            if c == '^':
                guard = y, x
                d = (-1, 0)
            if c == 'v':
                guard = y, x
                d = ( 1, 0)
            if c == '<':
                guard = y, x
                d = ( 0, -1)
            if c == '>':
                guard = y, x
                d = ( 0, 1)

            cols = x+1

readmp()

def run(extra):
    guard = iniguard
    d  = inid

    vis = set()
    k = 0
    while True:
        # print (guard, d)
        gy, gx = guard

        if gy < 0:
            break
        if gx < 0:
            break
        if gy >= rows:
            break
        if gx >= cols:
            break

        st = guard, d
        if st in vis:
            return True # loops
        vis.add(st)

        dy, dx = d

        ny, nx = gy + dy, gx + dx

        if (ny, nx) in walls or ((ny, nx) == extra):
            d = dx, -dy
            continue

        guard = ny, nx
    return False

l = 0
iniguard = guard
inid = d
for y in range(rows):
    for x in range(cols):
        print(y, x)
        l += run((y, x))

print(l)
