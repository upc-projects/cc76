import heapq as hq

def find(s, a):
    if s[a] < 0:
        return a
    else:
        granpa = find(s, s[a])
        s[a] = granpa
        return granpa

def union(s, a, b):
    pa = find(s, a)
    pb = find(s, b)
    if pa == pb: return
    
    if s[pa] <= s[pb]:
        s[pa] += s[pb]
        s[pb] = pa
    elif s[pb] < s[pa]:
        s[pb] += s[pa]
        s[pa] = pb


def makeIL(G):
    il = []
    n = len(G)
    for u in range(n):
        for v, w in G[u]:
            il.append((w, u, v))
    return il

def kruskal(G):
    il = makeIL(G)
    q = []
    n = len(G)
    for edge in il:
        hq.heappush(q, edge)
    roots = [-1]*n
    T = []
    while len(q) > 0:
        w, u, v = hq.heappop(q)
        if find(roots, u) != find(roots, v):
            union(roots, u, v)
            T.append((u, v, w))
    return roots, T

G = []
with open('unidad2/mst/grafito.in') as f:
    for line in f:
        u = len(G)
        G.append([])
        nums = [int(x) for x in line.split(' ')]
        for i in range(len(nums) // 2):
            G[u].append((nums[i * 2], nums[i * 2 + 1]))

print(kruskal(G))



