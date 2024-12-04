import fileinput
from collections import Counter

def take(word, n, k):
    if k == 0:
        yield []
        return
    if len(word) < n:
        return []

    h = word[:n]
    more = word[n:]

    for sub in take(more, n, k-1):
        yield h, *sub

    for sub in take(word[1:], n, k):
        yield sub



def case(word):
    print(word)
    vs = 0
    for l in word:
        if l in "aeiou":
            vs += 1

    pair = False
    pairs = list(take(word, 2, 2))
    for x, y in pairs:
        print(x, y)
        if x == y:
            pair = True

    bet = False
    for a, b, c in zip(word, word[1:], word[2:]):
        if a == c:
            bet = True

    return pair and bet


total = 0
for line in fileinput.input():
    total += case(line.strip())

print(total)
