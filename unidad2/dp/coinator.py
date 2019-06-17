#!/usr/bin/env python
# coding: utf-8

# In[3]:

import math
# In[14]:


def coins(d, n):
    C = [-1]*(n+1)
    S = [0]*(n+1)
    def f(p):
        if p <= 0:
            C[0] = 0
            return
        f(p-1)
        count = math.inf
        coin = 0
        for di in d:
            if di <= p:
                if C[p-di] < count:
                    count = C[p-di]
                    coin = di
        
        C[p] = count + 1
        S[p] = coin
    f(n)
    return C, S


# In[30]:


p = 19
c, s = coins([1, 5, 10, 20, 25, 50], p)


# In[31]:
print(c)
print(s)


# In[32]:


while p > 0:
    print(s[p])
    p -= s[p]


# In[ ]:




