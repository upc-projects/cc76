import heapq as hq
import math
import unidad2.mst.prim as prim


def dist(p1, p2):
    #return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**.5
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


points = []
with open('data.in') as f:
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


path, cost = prim.prim(G)
print(path)
print(cost)




