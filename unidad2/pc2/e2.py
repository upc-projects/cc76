import heapq as hq
import math

def find(t, a):
    if t[a] == a:
        return a
    else:
        abuelito = find(t, t[a])
        return abuelito

def union(t, a, b):
    pa = find(t,a)
    pb = find(t,b)
    t[pb] = pa

def Kruskal(G):
    n = len(G)
    q = []

    for u in range(n):
        for v, w in G[u]:
            hq.heappush(q, ((-1*w), u, v))
    
    Gf = [[] for _ in range(n)]
    uf = [i for i in range(n)]

    count = 0
    minVal = math.inf

    while(count != n-1):
        w, u, v = hq.heappop(q)
        pu = find(uf,u)
        pv = find(uf,v)

        if pu != pv:
            Gf[u].append((v,w*-1))
            if minVal > w*-1:
                minVal = w*-1
            union(uf, u, v)
            count +=1
            
    return Gf, minVal


#G = [[(1,10), (1,20), (0,30)],
#     []]

G = [[(2,5), (1,1)],
     [(2,3)],
     [(3,4)],
     [(1,2)]]

Gf, minVal = Kruskal(G)
print(minVal)

