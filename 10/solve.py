from lib import *

lines = inputlines()
rows, cols, mp, rmp = readmp(lines)
printmp(mp, rows, cols)

more = []
seen = set()
for p in rmp['0']:
    more.append((p, p))

end = set()
while more:
    (p, th), *more = more
    if (p, th) in seen:
        continue
    seen.add((p, th))
    c = mp[p]
    for n in neighs(p, nd4a):
        if inbounds(n, (0, 0), (rows, cols)):
            oc = mp.get(n, '.')
            if oc == chr(ord(c) + 1):
                if n not in seen:
                    more.append((n, th))
                    if oc == '9':
                        end.add((n, th))


s = 0
for (p, th) in end:
    print(p, th)
    s += 1



# s = 0
# for l in lines:
#     s += len(l)
# 
# print("?")
print(s)
