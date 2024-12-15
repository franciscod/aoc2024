from lib import *
# sys.setrecursionlimit(2999)

lines = inputlines()

mplines = []
mvlines = []

ilines = iter(lines)
for l in ilines:
    if l == "":
        break
    mplines.append(l)

mvlines = list(ilines)

rows, cols, mp, rmp = readmp(mplines)

mp2 = {}
for p, c in mp.items():
    py, px = p
    px1 = px*2
    px2 = px*2+1
    if c == '.':
        continue

    c2 = c
    c1 = c
    if c == 'O':
        c1, c2 = '[]'

    mp2[py, px1] = c1
    if c == '@':
        at = py, px1
        continue
    mp2[py, px2] = c2

cols = cols * 2
mp = mp2

rmp = {}


moves = []
for l in mvlines:
    for c in l:
        moves.append(c)

printmp(mp, rows, cols)
# print(moves)

cdirs = "^v<>"
nd4a = (
    (-1,  0),
    ( 1,  0),
    ( 0, -1),
    ( 0,  1),
)


def dopush(p, d, o=False, dry=False):
    c = mp.get(p)
    if c == None:
        return True
    if c == '#':
        return False
    if c not in '[]':
        raise ValueError(c)

    # print("dopush", c, p, d, o,dry)

    py, px = p
    dy, dx = d
    om = True
    if dy != 0:
        if not o:
            om = False
            if c == '[':
                op = py, px+1
            else:
                op = py, px-1

            if not dopush(op, d, True, True):
                return False
            if not dopush(p, d, True, True):
                return False

    ny, nx = py + dy, px + dx
    n = ny, nx

    if dy != 0 and not o:
        # print("okgo op")
        om = dopush(op, d, True, dry)
    if om and dopush(n, d, False, dry):
        if not dry:
            del mp[p]
            mp[n] = c
        return True
    return False



def domove(lf, d):
    #print("moving", lf, d)
    lfy, lfx = lf
    dy, dx = d
    ny, nx = lfy + dy, lfx + dx

    n = ny, nx

    clear = dopush(n, d)
    if clear:
        del mp[lf]
        mp[n] = '@'
        #print("moved")
        return n
    #print("stayed")
    return lf


DEBUG = False

for i, m in enumerate(moves):
    # print(i, m)
    if i == 7:
        DEBUG = True
    lf = at
    d = nd4a[cdirs.index(m)]
    at = domove(lf, d)
    # printmp(mp, rows, cols)


s = 0
for (py, px), c in mp.items():
    if c == '[':
        s += 100*py+px

print("?")
print(s)
