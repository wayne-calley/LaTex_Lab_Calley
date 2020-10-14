#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np

def rule1(dA):
    dQ = c*(dA)
    return dQ

c = 9.8
dA = 0.0001

dQ = rule1(dA)

print (dQ)


# In[10]:


def rule2(A,dA):
    dQ = c*m*(A**(m-1))*dA
    return dQ

c = 1
m = 2
A = 3
dA = .001

dQ = rule2(a,dA)

print (dQ)


# In[11]:


def rule3(dA, dB):
    dQ = np.sqrt(dA**2+dB**2)
    return dQ

dA = .1
dB = 1.1

errT = rule3(dA, dB)
print (errT)


# In[17]:


def rule4(dA, dB):
    dQ = Q*np.sqrt((m*(dA/A))**2+(n*(dA/B))**2)
    return dQ

m = 1
n = 1
A = .2083
B = 10.5
dA = .0001
db = .031
Q = .783

dQ = rule4(dA, dB)

print (dQ)


# # Rule 3
# $\delta Q = \sqrt{(\delta A)^2 + (\delta B)^2}$

# # Rule 4
# 
# $\delta Q = |Q|\sqrt{(m(\frac{\delta A} A)^2)+(n(\frac{\delta B} B)^2)}$
# 
# $\delta Q = .783\sqrt{(\frac{.0001}{.2083})^2+(\frac{.031}{10.5})^2}$

# In[ ]:




