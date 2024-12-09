from lib import *

lines = inputlines()
line = lines[0]

disk = []
for i, c in enumerate(line):
    n = int(c)
    fid = None
    if i % 2 == 0:
        fid = i//2

    disk.append((fid, n))

# print(disk)

def printdisk(disk):
    for f, s in disk:
        if f is None:
            f = '.'
        print(str(f) * s, end='')
    print()

def defrag(disk):
    nd = []
    i = len(disk) - 1
    while i > 0:
        fid, si = disk[i]
        if fid is not None:
            #print("trying", fid, si)
            moved = False
            for j in range(i):
                fjd, sj = disk[j]
                if fjd is not None:
                    continue
                if si <= sj:
                    # print("- moving!")
                    disk[j:j+1] = [(fid, si), (None, sj - si)]
                    disk[i+1] = (None, si)
                    # printdisk(disk)
                    moved = True
                    break
                if moved:
                    break
            else:
                pass#print("- staying.")
        i -= 1

    return (disk)

chk = list(defrag(disk))

def raw(disk):
    for f, s in disk:
        for _ in range(s):
            yield f

s = 0
for i, n in enumerate(raw(disk)):
    if n is None:
        continue
    s += i * n
print(s)

