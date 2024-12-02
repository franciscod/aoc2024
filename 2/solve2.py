import fileinput
from collections import Counter

def is_bad(ls):
    dif = [abs(a-b) for a, b in zip(ls, ls[1:])]
    inc = [a > b for a, b in zip(ls, ls[1:])]
    dec = [a < b for a, b in zip(ls, ls[1:])]
    bad = False
    if not all(inc) and not all(dec):
        bad = True
    for d in set(dif):
        if d not in set((1, 2, 3)):
            bad = True
    return bad

def try_fix(ls):
    if not is_bad(ls):
        return False

    # print(ls)
    for i in range(len(ls)):
        lls = ls[:i] + ls[i+1:]
        if not is_bad(lls):
            return False
        # print(lls)
    return True

ks = 0
for line in fileinput.input():
    ls = line.split()
    print(ls)
    ls = list(map(int, ls))
    bad = try_fix(ls)

    ks += not bad

print(ks)
