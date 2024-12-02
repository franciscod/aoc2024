import fileinput
from collections import Counter

ks = 0
for line in fileinput.input():
    ls = line.split()
    print(ls)
    ls = list(map(int, ls))
    dif = [abs(a-b) for a, b in zip(ls, ls[1:])]
    inc = [a > b for a, b in zip(ls, ls[1:])]
    dec = [a < b for a, b in zip(ls, ls[1:])]
    bad = False
    if not all(inc) and not all(dec):
        bad = True
    for d in set(dif):
        if d not in set((1, 2, 3)):
            bad = True

    ks += not bad

print(ks)
