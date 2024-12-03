import re
import fileinput
pattern = "mul\(([0-9]+),([0-9]+)\)"

ts = 0
en = True

def parse(os, i):
    global ts 
    global en

    s = os[i:]
    if not s:
        return

    if s.startswith('don\'t()'):
        en = False
        return

    if s.startswith('do()'):
        en = True
        return

    if not s.startswith("mul("):
        return
    
    m, p, rest = s.partition('(')
    j = len(m) + len(p)
    args, p, rest = rest.partition(')')
    j += len(m) + len(p)
    argss = args.split(',')
    if len(argss) == 2:
        a, b = argss
        try:
            a, b = int(a), int(b)
        except ValueError:
            return
        if en:
            ts += a*b
    else:
        return


for line in fileinput.input():
    l = line.strip()
    print(l)
    
    for i in range(len(l)):
        parse(l, i)
    print(ts)
