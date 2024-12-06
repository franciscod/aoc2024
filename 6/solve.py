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

vis = set()
k = 0
while True:
    print (guard, d)
    gy, gx = guard

    if gy < 0:
        break
    if gx < 0:
        break
    if gy >= rows:
        break
    if gx >= cols:
        break

    vis.add(guard)

    dy, dx = d

    ny, nx = gy + dy, gx + dx

    if (ny, nx) in walls:
        d = dx, -dy
        continue

    guard = ny, nx

print(len(vis))
