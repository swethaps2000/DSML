#!/usr/bin/env python
# coding: utf-8

# In[2]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


y=[5,3,4,5,6,7,2,8,9]
plt.plot(y)
plt.show()


# In[9]:


x=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
y=[i**2 for i in x]
plt.plot(x,y)
plt.show()


# In[12]:


import numpy as np
import math
x=np.arange(-1,1.1,0.1).tolist()
y=[i**2+5 for i in x]
print(x)
print(y)
plt.plot(x,y)
plt.show()


# In[22]:


import numpy as np
x=np.arange(0,10,0.1)
y=np.sin(x)
print(x)
print(y)

plt.plot(x,y)
plt.xlabel('angle')
plt.ylabel('sin')
plt.title('sin wave')
plt.show()


# In[48]:


plt.plot(x,y)
plt.scatter(x,y)
plt.xlabel('angle')
plt.ylabel('sin')
plt.title('sin wave')
plt.show()


# In[49]:


plt.plot(x,np.sin(x), 'b+',label='sin')
plt.plot(x,np.cos(x), 'y--',label='cos')
plt.xlabel('angle')
plt.ylabel('sin/cos')
plt.title('sin/cos wave')
plt.ylim(-2,2)
plt.xlim(-5,15)
plt.legend()
plt.show()


# In[50]:


fig,axis=plt.subplots(1,2,figsize=(10,5))
print(axis.shape)


# In[76]:


fig,axis=plt.subplots(1,2,figsize=(10,5))
x=np.arange(0,10,0.1)

axis[0].plot(x,np.sin(x),'y--')
axis[0].set_title('sin')
axis[0].set_xlabel('angle')
axis[0].set_ylabel('sin')


axis[1].plot(x,np.cos(x), 'r--')
axis[1].set_title('cos')
axis[1].set_xlabel('angle')
axis[1].set_ylabel('cos')


plt.show()


# In[114]:


fig,axis=plt.subplots(2,2,figsize=(10,10))
x=np.arange(0,10,0.1)

axis[0][0].plot(x,np.sin(x),'h--')
axis[0][0].set_title('sin')
axis[0][0].set_ylim(-3,3)

axis[0][1].plot(y,2*np.cos(x),'g--')
axis[0][1].set_title('cos')
axis[0][1].set_ylim(-3,3)

axis[1][0].plot(x,np.tan(x), 'r--')
axis[1][0].set_title('tan')
axis[1][0].set_ylim(-2,2)

axis[1][1].plot(x,2*np.cos(x), 'y--')
axis[1][1].set_title('cos')
axis[1][1].set_ylim(-4,4)
plt.show()


# In[122]:


x=np.random.random(100)*100
y=np.random.random(100)*100


# In[124]:


plt.scatter(x,y)
plt.xlabel('price')
plt.ylabel('demand')
plt.title('stock')
plt.show()


# In[143]:


x=np.array([1,2,3])
y=[5,85,50]
plt.bar(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Bar Chart')
plt.show()


# In[153]:


slice = [12, 25, 50, 36, 19] 
activities = ['NLP', 'Neural Network', 'Data analytics', 'Quantum Computing', 'Machine Learning']  
cols = ['r', 'b', 'c', 'g', 'orange'] 


plt.pie(slice,
        labels=activities,
        colors=cols,
        startangle=45,  
        shadow=True,  
        explode=(0, 0.1, 0,0, 0),  
        autopct='%3.1f%%'  
        )


plt.title('Training Subjects')


plt.show()


# In[9]:


days=[1,2,3,4,5]
age=[21,34,42,25,41]
weight=[50,62,63,55,88]
plt.plot([], [], color='b', label='Weather Predicted', linewidth=5)
plt.plot([], [], color='g', label='Weather Change happened', linewidth=5)
plt.stackplot(days, age, weight, colors=['c', 'g'])
plt.xlabel('Fluctuation with time')
plt.ylabel('Days')
plt.title('Weather Report using Area Plot')
plt.legend()
plt.show()


# In[10]:


pop = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 2, 8]
bins = [1, 10, 20, 30, 40, 50]
plt.hist(pop, bins, rwidth=1)
plt.xlabel('Age Groups')
plt.ylabel('Number of People')
plt.title('Histogram')
plt.show()


# In[ ]:




