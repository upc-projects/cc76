import math

def Bellman_ford(G):
    n = len(G)
    distance = [-math.inf]*n
    parents = [None]* n
    distance[0] = 0

    for _ in range(n-1):
        for u in range(n):
            for v, w in G[u]:
                if distance[v-1] < distance[u-1] + w:
                    distance[v-1] = distance[u-1] + w
                    parents[v-1] = u
    
    return distance ,parents

G = [[(2,0)],
     [(0,20), (3,20)],
     [(4,-60)],
     [(5,-60)],
     []]

win = True
distance, _  = Bellman_ford(G)

for i in distance:
    if i <= -100:
        win=False

print("winnable" if win else "hopeless")
