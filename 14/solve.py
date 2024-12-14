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

steps = 100
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
# pprint(robots)


# print(w, w//2)
k = Counter((py, px) for px, py, vx, vy in robots)
mp = {}
for p, amt in k.items():
    mp[p] = amt

# printmp(mp, h, w)

qk = Counter((py<h//2, px<w//2) for px, py, vx, vy in robots if px != w//2 and py != h//2)

s = 1
for q in qk.values():
    s *= q
print(s)
# 87972792 too low
