from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

locks = []
keys = []
s = 0
lls = [] 
def proc(lls):
    iskey = True
    if lls[0] == '#####':
        iskey = False

    rows, cols, mp, _ = readmp(lls)
    hs = []
    height = 0
    for x in range(cols):
        for y in range(rows):
            if iskey:
                y = 6-y
            if mp.get((y,x), '.') == '#':
                height = y
        if iskey:
            height = 6 - height
        hs.append(height)
    if iskey:
        keys.append(hs)
    else:
        locks.append(hs)

for l in lines:
    if l == "":
        proc(lls)
        lls = []
    else:
        lls.append(l)

def fit(k, l):
    for i, j in zip(k, l):
        if i+j >= 6:
            return False
    return True

proc(lls)
s = 0
for k in keys:
    for l in locks:
        if fit(k, l):
            s += 1

print("?")
print(s)
