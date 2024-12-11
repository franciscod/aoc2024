from lib import *

lines = inputlines()
rows, cols, mp, rmp = readmp(lines)
printmp(mp, rows, cols)

more = []
seen = set()
for p in rmp['0']:
    more.append((p, p, 0))

end = set()
while more:
    (p, th, bn), *more = more
    if (p, th, bn) in seen:
        continue
    seen.add((p, th, bn))
    c = mp[p]
    for ni, n in enumerate(neighs(p, nd4a)):
        nbn = bn * 4 + ni
        if inbounds(n, (0, 0), (rows, cols)):
            oc = mp.get(n, '.')
            if oc == chr(ord(c) + 1):
                if n not in seen:
                    more.append((n, th, nbn))
                    if oc == '9':
                        end.add((n, th, nbn))


s = 0
for t in end:
    print(t)
    s += 1



# s = 0
# for l in lines:
#     s += len(l)
# 
# print("?")
print(s)
