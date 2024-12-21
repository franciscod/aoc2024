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

@cache
def complexity(p, k, phase1):
    p1, a, p2 = p.partition("A")
    p1 = p1+"A"
    if p2 != '':
        # print(p)
        # print(p1, p2)
        return complexity(p1, k, phase1) + complexity(p2, k, phase1)

    if k == -1:
        lc = len(p)
        return lc

    kk = kk1 if phase1 else kk2

    aa = []
    comps = set()
    for n in shortest(p, kk):
        comps.add(complexity(n, k-1, False))
    return min(comps)

s = 0
for line in lines:
    ilr = int(line.replace('A',''))
    lcomp = complexity(line, 25, True)
    s += lcomp*ilr

print(s)
