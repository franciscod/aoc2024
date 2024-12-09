from lib import *

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)

s = 0
for l in lines:
    s += len(l)

print("?")
print(s)
