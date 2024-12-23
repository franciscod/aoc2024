from lib import *
# import networkx as nx
# sys.setrecursionlimit(2999)

lines = inputlines()
# rows, cols, mp, rmp = readmp(lines)
# rows, cols, mp, rmp = widemp(mp)
# printmp(mp, rows, cols)

s = 0

G = nx.Graph()
for l in lines:
    a, b = l.split('-')
    G.add_edge(a,b)

cq = sorted(nx.find_cliques(G), key=len)[-1]
print(','.join(sorted(cq)))
