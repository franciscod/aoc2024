from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
g = iter(lines)

known = set()
vals = {}
ops = {}
deps = defaultdict(set)
unlocks = defaultdict(set)
pend = set()

for l in g:
    if l == "":
        break
    a, b = l.split(': ')
    vals[a] = int(b)
    known.add(a)

# print("digraph {")

for l in g:
    ws = l.split()
    a, op, b, _, r = ws
    ops[r] = (op, a, b)
    # print(f"{a} -> {r}")
    # print(f"{b} -> {r}")
    known.add(a)
    known.add(b)
    known.add(r)
    pending = False
    deps[r].add(a)
    unlocks[a].add(r)
    deps[r].add(b)
    unlocks[b].add(r)
    if a not in vals:
        pending = True
    if b not in vals:
        pending = True

    if pending:
        pend.add(r)

# print("x -> y")
# print("y -> z")
# for l in "xyz":
#     print("{")
#     print("rank=same")
#     print(f"{l} -> {l}00")
#     for k in known:
#         if k[0] == l:
#             nk = k[0] + "{:02d}".format(int(k[1:])+1)
#             print(f"{k} -> {nk}")
# 
#     print("rankdir=LR")
#     print("}")
# print("}")

def ss(k):
    if k in vals:
        return

    for d in deps[k]:
        ss(d)

    op, ka, kb = ops[k]
    a = vals[ka]
    b = vals[kb]

    OPMAP = {
            'AND': (lambda a, b: a&b),
            'OR': (lambda a, b: a|b),
            'XOR': (lambda a, b: a^b),
            }

    vals[k] = OPMAP[op](a, b)

def reqsof(k):
    reqs = set()
    for d in deps[k]:
        reqs.add(d)
        for r in reqsof(d):
            reqs.add(r)
    return reqs


def opt(k):
    if k not in ops:
        return ("", k, )
    op, ka, kb = ops[k]
    ga = opt(ka)
    gb = opt(kb)
    ga, gb = sorted((ga, gb))
    return op, ga, gb

def zj(t):
    if type(t) != tuple:
        return t
    return ' '.join(zj(s) for s in t if s)

def fb(l, n):
    return l + "{:02d}".format(n)

def carrybit(n):
    if n == 0:
        return andbit(n)
    return "OR", andbit(n), ("AND", carrybit(n-1), xorbit(n))

def andbit(n):
    return "AND", fb("x", n), fb("y", n)

def xorbit(n):
    return "XOR", fb("x", n), fb("y", n)

def genadds(n):
    if n == 0:
        return xorbit(n)
    return 'XOR', carrybit(n-1), xorbit(n)

def checkadds(z, zo):
    n = int(z[1:])

    xb =   zj(xorbit(n))
    adds = zj(genadds(n))
    ab =   zj(andbit(n))
    cb =   zj(carrybit(n))

    print(ops[z])

    print(n, "xorb", opstrr[xb], ops[opstrr[xb]])
    print(n, "andb", opstrr[ab], ops[opstrr[ab]])
    print(n, "adds", opstrr[adds], ops[opstrr[adds]])
    print(n, "carr", opstrr[cb], ops[opstrr[cb]])



    zg = jg = genadds(n)
    zjo = zj(zo)
    zjg = zj(jg)
    if zjo == zjg:
        return True
    else:
        print("HMMM")
        if zjg in opstrr:
            print(z, opstrr[zjg])



def swapop(a, b):
    ops[a], ops[b] = ops[b], ops[a]

swapop('z14', 'hbk') #!!!
swapop('z18', 'kvn') #!!!
swapop('z23', 'dbb') #!!!
swapop('tfn', 'cvh') #!!!

opstr = {}
opstrr = {}

for k in known:
    s = zj(opt(k))
    opstr[k] = s
    opstrr[s] = k

def step():
    zs = set()
    oks = set()

    for k in known:
        if k.startswith('z'):
            if 'x'+k[1:] in known:
                if 'y'+k[1:] in known:
                    zs.add(k)

    for i, z in enumerate(sorted(zs)):
        zo = opt(z)
        ok = checkadds(z, zo)
        if not ok:
            print("fishy", z)
            sus = set()
            for r in reqsof(z):
                if r not in oks:
                    sus.add(r)
            return i,sus
        else:
            for r in reqsof(z):
                oks.add(r)
    return 999, None


watermark = 0
while True:
    i, sus = step()
    if i > watermark:
        watermark = i
    break

#     print(len(sus), sus)
#     tryfix(sus, i)
#     for a, b in pairs(sus):
#         if a in ops:
#             if b in ops:
#                 ops[a], ops[b] = ops[b], ops[a]
#                 fi, fsus = step()
#                 print(" ", fi, len(fsus))
#                 if fi > watermark:
#                     print("OMG", a, b)
#                 else:
#                     ops[a], ops[b] = ops[b], ops[a]

    break


print(','.join(sorted(('z14', 'hbk', 'z18', 'kvn', 'z23', 'dbb', 'tfn', 'cvh'))))
