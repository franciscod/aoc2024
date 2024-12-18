from lib import *
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

data = '\n'.join(lines)
state = parse("""Register A: {:d}
Register B: {:d}
Register C: {:d}

Program: {}""", data)
a, b, c, program = state
insns = parseints(program, ',')
machine = (a, b, c, 0, insns)

def combo(op, machine):
    if op <= 3: return op
    if op == 4: return machine[0]
    if op == 5: return machine[1]
    if op == 6: return machine[2]
    if op == 7: raise ValueError("Reserved")
    raise NotImplementedError

def xc(machine):
    # print("xc", machine)
    a, b, c, ip, insns = machine
    if len(insns) == ip:
        raise IndexError
    ins, oper = insns[ip:ip+2]
    lit = oper
    if ins == 0: # adv
        cb = combo(oper, machine)
        # print(f"adv    a = a << {cb}")
        a = a // 2**cb
        return a, b, c, ip+2, insns, []

    if ins == 1: # bxl
        # print(f"bxl    b = b ^ {lit}")
        b = b ^ lit
        return a, b, c, ip+2, insns, []

    if ins == 2: # bst
        cb = combo(oper, machine)
        b = cb % 8
        # print(f"bst    b = {cb} % 8")
        return a, b, c, ip+2, insns, []

    if ins == 3: # jnz
        # print(f"jnz    {a}")
        if a == 0:
            return a, b, c, ip+2, insns, []
        else:
            return a, b, c, lit, insns, []

    if ins == 4: # bxc
        # print(f"bxc    b = b ^ {c}")
        b = b ^ c
        return a, b, c, ip+2, insns, []

    if ins == 5: # out
        cb = combo(oper, machine)
        # print(f"out    {cb}")
        return a, b, c, ip+2, insns, [cb % 8]

    if ins == 6: # bdv
        # print(f"bdv    b = a << {cb}")
        cb = combo(oper, machine)
        b = a // 2**cb
        return a, b, c, ip+2, insns, []

    if ins == 7: # cdv
        cb = combo(oper, machine)
        # print(f"cdv    c = a << {cb}")
        c = a // 2**cb
        return a, b, c, ip+2, insns, []

    raise IndexError

def inspect(a, best):
    print("? ", best, oct(a))

    clues = {}
    i = 0
    while a:
        la = a & 7
        li = la^3
        print("i: ", i*3,  7 & a,
              "li:", i*3+li, 7 & (a >> li))
        clues[i*3] = 7&a
        clues[i*3+li] = 7&(a >> li)
        a = a >> 3
        i += 1
    return clues

def crank2(machine):
    a, b, c, *rest = machine
    i = 0
    while (a >> 3*i) != 0:
        i0 = 3*i
        ai0 = a >> i0 & 7

        i1 = i0 + (ai0 ^ 3)
        ai1 = a >> i1 & 7

        b6 = 6 ^ ai0 ^ ai1
        yield b6, ((i0, ai0), (i1, ai1))

        i += 1

def crank(machine):
    while True:
        try:
            omachine = machine
            *machine, out = xc(machine)
        except IndexError:
            # print("HALT")
            break
        if out:
            yield from out

def f(a):
    if a == 0:
        return 0, 0

    na = a >> 3

    i0 = 0
    ai0 = a >> i0 & 7

    i1 = i0 + (ai0 ^ 3)
    ai1 = a >> i1 & 7

    b6 = 6 ^ ai0 ^ ai1
    return b6, na

def matchsufflen(a, b):
    l = 1
    while True:
        if a[-l:] != b[-l:]:
            return l-1
        l += 1

imachine = machine
insns = tuple(insns)

bestlen = 0
# known values of A matching suffix of len K
knowns = defaultdict(set)
knowns[bestlen].add(0)

suffix = {}
suffix[0] = True

for a in range(0o10000):
    gas = tuple(crank((a, 0, 0, 0, insns)))
    nl = len(gas)
    g = gas[0]

    suffix[a] = insns[-nl:] == gas
    if suffix[a]:
        knowns[nl].add(a)
        bestlen = nl
        # print(a, gas)


print(insns)
search = True
while search:
    search = False
    for b in knowns[bestlen]:
        # print(bestlen, b)
        for od in range(3):
            for c in range(1<<od*3):
                # print(bestlen, b, c)
                a = b << od*3 | c


                gas = tuple(crank((a, 0, 0, 0, insns)))
                nl = len(gas)
                g = gas[0]
                na = a >> 3

                suffix[a] = insns[-nl:] == gas

                if nl > bestlen:
                    bestlen = nl
                    search = True

                if suffix[a]:
                    knowns[nl].add(a)
                    gas = tuple(crank((a, 0, 0, 0, insns)))
                    # print(g, gas)
                    if gas == insns:
                        print(a)
                        exit(0)

# 23070159490600
# TOO LOW
# 216584205979245
# TOO HIGH
# 234176392023743
