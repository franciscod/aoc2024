from lib import *

lines = inputlines()
rows, cols, mp, rmp = readmp(lines)

rn = 0
regs = dict()

def flood(reg, p, seen):
    if p in seen:
        return

    regs[p] = reg
    seen.add(p)

    y, x = p

    pl = y, x-1
    pu = y-1, x
    pr = y, x+1
    pd = y+1, x

    cl = mp.get(pl)
    cu = mp.get(pu)
    cr = mp.get(pr)
    cd = mp.get(pd)
    if c == cl:
        flood(reg, pl, seen)
    if c == cu:
        flood(reg, pu, seen)
    if c == cd:
        flood(reg, pd, seen)
    if c == cr:
        flood(reg, pr, seen)


for y in range(rows):
    print("y", y)
    for x in range(cols):
        p = y,x
        c = mp.get(p)
        print(c)

        if regs.get(p) is None:
            reg = rn
            print("new", reg)
            rn += 1
            flood(reg, p, set())

sger = defaultdict(set)
for p, r in regs.items():
    sger[r].add(p)

def calcperi(ps):
    peri = 0
    for p in ps:
        for neigh in neighs(p, nd4a):
            if regs.get(neigh) != regs[p]:
                peri += 1
    return peri

s = 0
for r, ps in sger.items():
    #print(r, ps)
    area = len(ps)
    peri = calcperi(ps)
    pri = area * peri
    s += pri
    print(mp[next(iter(ps))], area, peri, '=', pri)

print(s)