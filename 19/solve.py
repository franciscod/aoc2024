from lib import *
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)
available = lines[0].split(', ')


@cache
def possible(d):
    print(d)
    if d == '':
        return True

    for t in available:
        if d.startswith(t):
            r = d[len(t):]
            if possible(r):
                return True

    return False


s = 0
for d in lines[2:]:
    print("#", d)
    if possible(d):
        s += 1

print(s)
