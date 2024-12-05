import fileinput
from collections import defaultdict
from functools import cmp_to_key

rules = []
prods = []

after = defaultdict(set)

for line in fileinput.input():
    line = line.strip()
    if line == '':
        continue
    if '|' in line:
        rules.append(tuple(map(int, line.split('|'))))
    else:
        prods.append(list(map(int, line.split(','))))

for x, y in rules:
    after[x].add(y)
    print(x, y)


def check(upd):
    for i in range(0, len(upd)-1):
        for j in range(i+1, len(upd)):
            a, b = upd[i], upd[j]
            if a in after[b]:
                return False
    return True

def cmpafter(x, y):
    if x == y:
        return 0
    if x not in after[y]:
        return -1
    else:
        return 1

def fix(upd):
    return list(sorted(upd, key=cmp_to_key(cmpafter)))

tot = 0
for upd in prods:
    if not check(upd):
        print("fixing", upd)
        upd = fix(upd)
        print(":> ", upd)
        tot += upd[len(upd)//2]

print(tot)
