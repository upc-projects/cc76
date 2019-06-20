import heapq as hq
import math

def bellmanford(G, s):
    n = len(G)
    d = [math.inf]*n
    p = [None]*n
    d[s] = 0
    for _ in range(n-1):
        for u in range(n):
            for v, w in G[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    p[v] = u
        
    for u in range(n):
        for v, w in G[u]:
            if d[v] > d[u] + w:
                print("Oh no!, ciclo negativo")
                return
    return p, d

G = [[(1, 6), (3, 7)],
     [(2, 5), (3, 8), (4, -4)],
     [(1, -2), (4, 7)],
     [(2, -3), (4, 9)],
     [(0, 2)]]

print(bellmanford(G, 0))
