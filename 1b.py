#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
x=np.array([1,2,3,4])
print(x)
print(type(x))
print(x.shape)


# In[10]:


import numpy as np
y=np.array([[1,2],[3,4]])
print(y)
print(y.shape)


# In[12]:


import numpy as np
z=np.array([[1+0.j,2+0.j]])
print(z)
print(z.shape)


# In[58]:


a=np.zeros((2,3))
print(a)
print(a.shape)
b=np.ones((2,2),dtype=int)
print(b)


# In[17]:


d=np.eye(3)
print(d)


# In[21]:


e=np.arange(10)
print(e)


# In[22]:


e=np.arange(12,21)
print(e)


# In[23]:


e=np.arange(5,20,3)
print(e)


# In[29]:


f=np.linspace(1,10,9)
print(f)


# In[31]:


g=np.random.random((3,4))
print(g)


# In[33]:


h=np.random.random((3,4))
print(h.reshape(2,2,3))


# In[40]:


x=np.arange(12)
print(x)
print(x[0])
print(x[4])
print(x[-1])
x.resize(3,4)
print(x)
print(x[-1,-1])
print(x[2][3])


# In[60]:


y=np.arange(1,26)
print(y)
print(y[:3])
print(y[10:])
print(y[10:15])
print(y[-5:])
print(y[3:-3])
print(y[::3])
print(y.reshape(5,5))
print(y)
y=y.reshape(5,5)
print(y)
print(y[:3,:3])
print(y[2:-1,1:-1])
print(y[:,:-1])
print(y[:,-1])
print(y[::,::3])


# In[62]:


print(y)
print(y[1::2,1::2])


# In[67]:


a=np.arange(1,6)
b=np.arange(6,11)
print(a)
print(b)
print(a+b)
print(a-b)
print(b-a)
print(a**2)


# In[68]:


print(a>3)


# In[72]:


a=np.arange(0,4).reshape((2,2))
print(a)


# In[76]:


b=np.eye(2)
print(b)
print(a*b)


# In[77]:


print(np.dot(a,b))


# In[79]:


x=np.arange(1,10).reshape((3,3))
print(x)


# In[81]:


print(x.sum())


# In[82]:


print(x.sum(axis=0))


# In[83]:


print(x.sum(axis=1))


# In[84]:


x=np.arange(1,19).reshape((3,3,2))
print(x)


# In[85]:


print(x.sum(axis=0))


# In[86]:


print(x.sum(axis=1))


# In[92]:


x=np.arange(1,10).reshape((3,3))
print(x)
print(x.max())
print(x.max(axis=1))
print(x.max())
print(x.transpose())


# In[ ]:





# In[ ]:




