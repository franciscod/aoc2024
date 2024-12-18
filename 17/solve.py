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
        a = a // 2**cb
        return a, b, c, ip+2, insns, []

    if ins == 1: # bxl
        b = b ^ lit
        return a, b, c, ip+2, insns, []

    if ins == 2: # bst
        cb = combo(oper, machine)
        b = cb % 8
        return a, b, c, ip+2, insns, []

    if ins == 3: # jnz
        if a == 0:
            return a, b, c, ip+2, insns, []
        else:
            return a, b, c, lit, insns, []

    if ins == 4: # bxc
        b = b ^ c
        return a, b, c, ip+2, insns, []

    if ins == 5: # out
        cb = combo(oper, machine)
        return a, b, c, ip+2, insns, [cb % 8]

    if ins == 6: # bdv
        cb = combo(oper, machine)
        b = a // 2**cb
        return a, b, c, ip+2, insns, []

    if ins == 7: # cdv
        cb = combo(oper, machine)
        c = a // 2**cb
        return a, b, c, ip+2, insns, []

    raise IndexError

output = []
while True:
    print(machine)
    # input("step?")
    try:
        omachine = machine
        *machine, out = xc(machine)
    except IndexError:
        print("HALT")
        break
    if out:
        print("->", out)
        output += out

    # if machine == omachine:
    #     print("LOOP")
    #     break
    

s = ','.join(str(n) for n in output)
print(s)
