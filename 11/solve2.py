from lib import *

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)

s = 0
for l in lines:
    s += len(l)

t = 0
numnext = False

nums = parseints(lines[0])

# DUH PARA QUE PARSEE ESTO!!!
# for line in lines:
#     if line.startswith('Initial'):
#         t = 0
#         numnext = True
#         continue
#     if line.startswith('After'):
#         t = int(line.split()[1])
#         numnext = True
#         continue
#     if numnext:
#         nums = list(map(int, line.split()))
#         print(nums, t)
#         numnext = False
#         continue

def rule(s):
    if s == 0:
        return [1]
    kd = len(str(s))
    if kd % 2 == 0:
        return [int(str(s)[:kd//2]), int(str(s)[kd//2:])]
    return [2024 * s]

def apply(ss):
    nss = Counter()
    for s, k in ss.items():
        rs = rule(s)
        for r in rs:
            nss[r] += k
    return nss

nums = Counter(nums)

for i in range(75):
    nums = apply(nums)

print(sum(nums.values()))
