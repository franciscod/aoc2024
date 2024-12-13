from lib import *

sys.setrecursionlimit(2999)


lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)

def pmach(lines):
    ba = None
    bb = None
    p = None
    for line in lines:
        if line == "":
            continue
        b, xy = line.split(': ')
        if b == "Button A":
            x, y = xy.split(', ')
            x = int(x.split('+')[1])
            y = int(y.split('+')[1])
            ba = x, y
        if b == "Button B":
            x, y = xy.split(', ')
            x = int(x.split('+')[1])
            y = int(y.split('+')[1])
            bb = x, y
        if b == "Prize":
            x, y = xy.split(', ')
            x = int(x.split('=')[1])
            y = int(y.split('=')[1])
            pp = x, y
            yield (ba, bb, pp)

        # print(b, xy)

machines = list(pmach(lines))

@lru_cache
def f(mach):
    ba, bb, pp = mach
    ax, ay = ba
    bx, by = bb
    px, py = pp

    if (px, py) == (0, 0):
        return True, 0
    if px < 0:
        return False, 0
    if py < 0:
        return False, 0

    cands = set()
    pa, ca = f((ba, bb, (px-ax, py-ay)))
    if pa:
        cands.add(ca+3)
    pb, cb = f((ba, bb, (px-bx, py-by)))
    if pb:
        cands.add(cb+1)

    if len(cands) == 0:
        return False, 0
    
    return True, min(cands)

def best(mach):
    ba, bb, pp = mach

    ax, ay = ba
    bx, by = bb

    px, py = pp

    kax = px//ax+1
    kay = py//ay+1
    kbx = px//bx+1
    kby = py//by+1
    la = max(kax, kay)+2
    lb = max(kbx, kby)+2
    print(f"{la=}")
    print(f"{lb=}")

    cands = set()
    for a in range(0, la):
        for b in range(0, lb):
            tx = a*ax + b*bx - px
            ty = a*ay + b*by - py
            if tx == 0 and ty == 0:
                cands.add(a * 3 + b)

    if not cands:
        return 0

    return min(cands)


s = 0
for m in machines:
    print(m)
    c = best(m)
    print(c)
    s += c

print(s)
