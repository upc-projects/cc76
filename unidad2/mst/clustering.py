import heapq as hq


# ## Find con compresión de path

def find(s, a):
    if s[a] < 0:
        return a
    else:
        granpa = find(s, s[a])
        s[a] = granpa
        return granpa


# # Quickunion ponderado

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

def clustering(G, k):
    n = len(G)
    q = []
    for u in range(n):
        for v, w in G[u]:
            hq.heappush(q, (w, u, v))
    roots = [-1]*n
    T = []
    numKlusters = n
    while len(q) > 0:
        w, u, v = hq.heappop(q)
        if find(roots, u) != find(roots, v):
            union(roots, u, v)
            T.append((u, v, w))
            numKlusters -= 1
            if numKlusters == k:
                break
    return roots, T


def dist(p1, p2):
    #return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**.5
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


points = []
with open('unidad2/mst/data.in') as f:
    for line in f:
        point = [int(x) for x in line.split(' ')]
        points.append((point[0], point[1]))
        
n = len(points)
G = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            G[i].append((j, dist(points[i], points[j])))
for i in range(n):
    print(i, points[i])

print(clustering(G, 3))
