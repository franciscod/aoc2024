import fileinput
from itertools import product

data = []

for line in fileinput.input():
    line = line.strip()
    a, r = line.split(':')
    a = int(a)
    r = list(map(int, r.split()))
    data.append((a, r))

t = 0
for r, ns in data:
    print(r, ns)
    for ops in product('+*C', repeat=len(ns)-1):
        re = ns[0]
        for o, n in zip(ops, ns[1:]):
            if o == '+':
                re += n
            elif o == '*':
                re *= n
            elif o == 'C':
                re = int(f"{re}{n}")

        if re == r:
            t += r
            break
print(t)
