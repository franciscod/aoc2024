from lib import *

rules = []
prods = []

after = defaultdict(set)

for line in inputlines():
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
    print("CHECKING", upd)
    for i in range(0, len(upd)-1):
        for j in range(i+1, len(upd)):
            a, b = upd[i], upd[j]
            print(a, b)
            if a in after[b]:
                return False
    return True

tot = 0
for upd in prods:
    if check(upd):
        tot += upd[len(upd)//2]

print(tot)
