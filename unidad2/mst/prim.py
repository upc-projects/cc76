#!/usr/bin/env python
# coding: utf-8

# In[17]:


import heapq as hq
import math
INF = float("inf")


# In[18]:


print(math.inf, INF)


# In[26]:


def prim(G):
    n = len(G)
    Known = [False]*n
    Cost = [math.inf]*n
    Path = [-1]*n
    queue = []
    s = 0
    Cost[s] = 0
    hq.heappush(queue, (0, s))
    while len(queue) > 0:
        _, u = hq.heappop(queue)
        if not Known[u]:
            Known[u] = True
            for v, w in G[u]:
                if not Known[v] and w < Cost[v]:
                    Cost[v] = w
                    Path[v] = u
                    hq.heappush(queue, (w, v))
                    
    return Path, Cost


# In[27]:


G = []
with open('grafito.in') as f:
    for line in f:
        u = len(G)
        G.append([])
        nums = [int(x) for x in line.split(' ')]
        for i in range(len(nums) // 2):
            G[u].append((nums[i * 2], nums[i * 2 + 1]))


# In[28]:


print(prim(G))


# In[29]:


q = []


# In[3]:


hq.heappush(q, 5)
hq.heappush(q, 9)
hq.heappush(q, 3)
hq.heappush(q, 1)
hq.heappush(q, 2)
hq.heappush(q, 8)
hq.heappush(q, 4)
hq.heappush(q, 6)
hq.heappush(q, 7)


# In[4]:


while len(q) > 0:
    print(hq.heappop(q))


# In[9]:


q = []


# In[10]:


hq.heappush(q, (5, "Sebastian"))
hq.heappush(q, (9, "Eduardo"))
hq.heappush(q, (3, "Daniel"))
hq.heappush(q, (1, "Adriana"))
hq.heappush(q, (2, "Rosario"))
hq.heappush(q, (8, "Fiscal"))
hq.heappush(q, (4, "otra cosa"))
hq.heappush(q, (6, 1999))
hq.heappush(q, (7, {"nombre": "Perez"}))


# In[11]:


while len(q) > 0:
    priority, elem = hq.heappop(q)
    print(priority, elem)


# In[ ]:




