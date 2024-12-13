import fileinput
import sys

from pprint import pprint

from collections import Counter
from collections import defaultdict
from itertools import combinations
from itertools import product
from functools import cmp_to_key
from functools import lru_cache

from sympy.solvers import solve
from sympy import Symbol
from sympy.core.numbers import Integer

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


nd8 = (
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0, -1),
    ( 0,  1),
    ( 1, -1),
    ( 1,  0),
    ( 1,  1),
)

nd4d = (
    (-1, -1),
    (-1,  1),
    ( 1, -1),
    ( 1,  1),
)

nd4a = (
    (-1,  0),
    ( 1,  0),
    ( 0, -1),
    ( 0,  1),
)


def dopp(d):
    dy, dx = d
    return -dy, -dx

def neighs(p, ns):
    py, px = p
    for n in ns:
        ny, nx = n
        yield (py+ny, px+nx)

def neighsd(p, ns):
    py, px = p
    for n in ns:
        ny, nx = n
        yield (py+ny, px+nx), n

def parseints(s):
    return list(map(int, s.split()))
