#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fiboMAL(n):
    if n < 2:
        return n
    else:
        return fiboMAL(n - 1) + fiboMAL(n - 2)


# In[2]:


def fibo(n):
    tab = [0] * (n+1)
    def f(n):
        if n < 2:
            tab[0] = 0
            tab[1] = 1
        else:
            f(n-1)
            tab[n] = tab[n-1] + tab[n-2]
    f(n)

    return tab[n]


# In[ ]:


# get_ipython().run_line_magic('timeit', 'fiboMAL(50)')


# # In[5]:


# get_ipython().run_line_magic('timeit', 'fibo(50)')


# In[ ]:




