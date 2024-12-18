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


def crank2(machine):
    a, b, c, *rest = machine
    while a != 0:
        b = a & 0b111 # bst a
        b = b ^ 0b011
        c = a >> b
        b = b ^ 0b101
        a = a >> 3
        b = b ^ c
        yield b & 0b111

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

output = []
imachine = machine
best = 0

for a in range(9999999999):
    machine = a, *imachine[1:]
    progress = 0
    for got, expected in zip(crank2(machine), insns):
        # print(got, expected)
        if got == expected:
            progress += 1
        else:
            break
    if progress == best:
        print(a, end=", ", flush=True)
    if progress > best:
        best = progress
        print("!")
        print(a, progress, "/", len(insns))
        print("--0>", oct(a))
        print("--1>", oct(a << 1))
        print("--2>", oct(a << 2))
        print("--3>", oct(a << 3))
        if best == len(insns):
            print(a)
            exit(0)
            
