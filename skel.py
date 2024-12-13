from lib import *
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)

s = 0
for l in lines:
    s += len(l)

print("?")
print(s)
