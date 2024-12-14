from lib import *
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)

orobots = []
s = 0
for l in lines:
    px, py, vx, vy = parse("p={:d},{:d} v={:d},{:d}", l)
    orobots.append((px, py, vx, vy))

w,h = 101, 103
# w,h = 11,7 TOO LOW!

for steps in range(101*103):

    nr = []
    mp = {}
    for r in orobots:
        px, py, vx, vy = r
        px += vx*steps + w*steps
        py += vy*steps + h*steps
        px %= w
        py %= h
        nr.append((px, py, vx, vy))
    robots = nr
    k = Counter((py, px) for px, py, vx, vy in robots)

    mp = {}
    for p, amt in k.items():
        mp[p] = amt
    kn = 0
    for p, amt in k.items():
        for n in neighs(p, nd8):
            if mp.get(n, 0) > 0:
                kn += 1
    if kn > 500:
        printmp(mp, h, w)
        print(steps)
        break
