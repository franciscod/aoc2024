import fileinput

def case(word):
    print(word)
    vs = 0
    for l in word:
        if l in "aeiou":
            vs += 1

    repe = False
    for ab in zip(word, word[1:]):
        a, b = ab
        s = ''.join(ab)
        print(s, a, b)
        if a == b:
            repe = True

        if s in ('ab', 'cd', 'pq', 'xy'):
            print("ban")
            return False

    return vs >= 3 and repe


k = 0
for line in fileinput.input():
    k += case(line.strip())

print(k)
