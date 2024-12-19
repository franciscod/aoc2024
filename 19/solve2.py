from lib import *
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)
available = lines[0].split(', ')


@cache
def ways(d):
    if d == '':
        return 1

    w = 0
    for t in available:
        if d.startswith(t):
            r = d[len(t):]
            w += ways(r)

    return w


s = 0
for d in lines[2:]:
    print("#", d)
    s += ways(d)

print(s)
