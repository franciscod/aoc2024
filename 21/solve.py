from lib import *
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

def cf(ps):
    return tuple(ps)

@cache
def pcomb(ps):
    if not ps:
        return ['']

    p0, *ps = ps
    ps = cf(ps)

    rs = []
    if not p0:
        p0 = [""]
    for p in p0:
        pre = p + "A"
        for rest in pcomb(ps):
            opt = pre + rest
            rs.append(opt)

    return rs

def shortest(line, kk):
    s = []
    aline = "A" + line
    for a, b in zip(aline, aline[1:]):
        paths = tuple(kk[a,b])
        s.append(paths)

    lpcs = tuple(pcomb(tuple(s)))
    return lpcs 

rows1, cols1, mp1, rmp1 = readmp([
    '789',
    '456',
    '123',
    '_0A',
])

rows2, cols2, mp2, rmp2 = readmp([
    '_^A',
    '<v>',
])

def calckk(mp, rmp):
    kk = defaultdict(set)
    for k, p in rmp.items():
        p = list(p)[0]
        o = p

        dist = dict()
        more = [(p, '', mp[p])]
        while more:
            (p, s, vis), *more = more
            if p in dist:
                if dist[p] < len(s):
                    continue
            dist[p] = len(s)
            if s:
                k = mp[o], mp[p]
                kk[k].add(s)
                # print(k, s)
            for n, d in neighsd(p, nd4a):
                c = mp.get(n, "_")
                if c in vis:
                    continue
                if c != "_":
                    more.append((n, s+d2c(d), vis+c))
    return kk

kk1 = calckk(mp1, rmp1)
kk2 = calckk(mp2, rmp2)

s = 0
for line in lines:
    lcomp = 99999999999

    for a in shortest(line, kk1):
        # print(line, a)
        for b in shortest(a, kk2):
            # print(a, b)
            for c in shortest(b, kk2):
                lc = len(c)
                ilr = int(line.replace('A',''))
                p = lc * ilr
                lcomp = min(lcomp, p)
    s += lcomp

print(s)
