from lib import *

lines = inputlines()
# mp = readmp(lines)

s = 0
for l in lines:
    s += len(l)

print("?")
print(s)
