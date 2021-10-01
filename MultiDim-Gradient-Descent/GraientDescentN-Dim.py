#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[20]:


import pandas as pd


# In[55]:


df = pd.read_csv('train.csv')


# In[56]:



y_train = df[' Y'].values
df.drop(labels =' Y',inplace=True,axis=1)
df['coef'] = [1 for i in range(379)]


# In[65]:


x_train = df.values


# In[59]:


y_train.shape


# In[194]:


def cost(m):
    ct = (1/379)*((y_train.reshape(-1,1) - x_train.dot(m))**2).sum()
    return ct


# In[195]:


def step_grad(alpha,m):
    der = x_train.T.dot(x_train.dot(m)-y_train.reshape(-1,1))
    m = m-alpha*der
    return m


# In[216]:


def run():
    m = np.zeros((14,1))
    alpha = 0.0001
#     print(m)
    for i in range(100000):
        m = step_grad(alpha,m)
        print(cost(m))
#         print(m)
        print(100*'*')
    return m


# In[217]:


run()


# In[219]:


m = np.array([[-9.38080766e-01],
      [ 7.41034435e-01],
      [ 1.16915696e-02],
      [ 7.80873721e-01],
      [-2.17455750e+00],
      [ 2.35429653e+00],
      [ 1.23338097e-01],
      [-2.95232355e+00],
      [ 2.53296817e+00],
      [-1.70290370e+00],
      [-2.25151962e+00],
      [ 5.88354286e-01],
      [-4.26368155e+00],
      [ 2.26772333e+01]])


# In[ ]:




