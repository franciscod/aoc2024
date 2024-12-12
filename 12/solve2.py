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

def calcsides(ps):
    sides = set()
    for p in ps:
        for neigh, d in neighsd(p, nd4a):
            if regs.get(neigh) != regs[p]:
                y, x = p
                dy, dx = d
                sides.add((y + dy*0.25, x + dx*0.25))

    sideregs = {}
    def sflood(sreg, s, seen):
        if s in seen:
            return

        sideregs[s] = sreg
        seen.add(s)
        for neigh, d in neighsd(s, nd4a):
            if neigh in sides:
                sflood(sreg, neigh, seen)

    srn = 0
    for s in sides:
        if s not in sideregs:
            sreg = srn
            srn += 1
            sflood(sreg, s, set())

    return srn



s = 0
for r, ps in sger.items():
    # print(r, ps, '_____')
    area = len(ps)
    peri = calcsides(ps)
    pri = area * peri
    s += pri
    print(mp[next(iter(ps))], area, peri, '=', pri)

print(s)
