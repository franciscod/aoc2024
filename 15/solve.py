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


def dopush(p, d):
    c = mp.get(p)
    if c == None:
        return True
    if c == '#':
        return False
    if c != 'O':
        raise ValueError(c)

    py, px = p
    dy, dx = d
    ny, nx = py + dy, px + dx
    n = ny, nx
    if dopush(n, d):
        del mp[p]
        mp[n] = 'O'
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



at = rmp['@'].pop()
for m in moves:
    lf = at
    d = nd4a[cdirs.index(m)]
    at = domove(lf, d)
    # printmp(mp, rows, cols)


s = 0
for (py, px), c in mp.items():
    if c == 'O':
        s += 100*py+px

print("?")
print(s)
