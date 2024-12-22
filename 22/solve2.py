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

def bestseq(cpss):
    rev = defaultdict(int)
    seqin = defaultdict(set)
    acs = set()
    for i, cps in enumerate(cpss):
        for seq in zip(cps, cps[1:], cps[2:], cps[3:]):
            price = seq[3][1]
            cs = tuple(i[0] for i in seq)
            if (cs,i) in rev:
                continue
            acs.add(cs)
            rev[cs,i] = price
            seqin[cs].add(i)

    mrev = 0
    mcs = []
    for cs in acs:
        srev = sum(rev[cs,i] for i in range(len(cpss)))
        if srev > mrev:
            mrev = srev
            mcs = cs
    return mcs, mrev
       
s = 0
cpss = []
for l in lines:
    n = int(l)
    oldprice = n % 10
    cps = []
    for _ in range(2000):
        on = n
        n = grow(n)
        price = n % 10
        change = price - oldprice
        oldprice = price
        cps.append((change, price))
    cpss.append(cps)

seq, s = bestseq(cpss)

print("?")
print(s)

# 1474
# 1768
