from lib import *

lines = inputlines()
line = lines[0]
print(line)

disk = []
for i, c in enumerate(line):
    n = int(c)
    fid = None
    if i % 2 == 0:
        fid = i//2
    for _ in range(n):
        disk.append(fid)

print(disk)

def defrag(disk):
    nd = []
    i = 0
    j = len(disk) - 1
    while i <= j:
        if disk[i] is not None:
            yield disk[i]
        else:
            while disk[j] is None:
                j -= 1
            yield disk[j]
            j -= 1
        i += 1


chk = list(defrag(disk))
print(chk)

s = 0
for i, n in enumerate(chk):
    s += i * n
print(s)

