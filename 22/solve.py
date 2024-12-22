from lib import *

# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

def mix(n, g):
    x = n^g
    return x

def prune(n):
    return n % 16777216

def grow(n):
    rm = n * 64
    n = mix(n, rm)
    n = prune(n)

    rd = n // 32
    n = mix(n, rd)
    n = prune(n)

    rm = n * 2048
    n = mix(n, rm)
    n = prune(n)
    return n

s = 0
for l in lines:
    n = int(l)
    for _ in range(2000):
        n = grow(n)
    s += n

print("?")
print(s)
