import fileinput
from collections import Counter

la = list()
lb = list()

ka = Counter()
kb = Counter()
for line in fileinput.input():
    ds = line.split()
    a = int(ds[0])
    b = int(ds[1])
    print(a, b)
    la.append(a)
    lb.append(b)
    ka[a] += 1
    kb[b] += 1

d = 0
s = 0
for a, b in zip(sorted(la), sorted(lb)):
    d += abs(a-b)
    s += a * kb[a]

print(d)
print(s)
