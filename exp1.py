#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=5
print(a)
print(type(a))
b=6.7
print(b)
print(type(b))
c=complex(2,5)
print(c)
print(type(c))


# In[12]:


c='beautiful'
d='flower'
print(c)
print(type(c))
print(c[0])
print(c[2:5])
print(c[2:])
print(c+" "+d)
print(c*2)


# In[13]:


a=True
b=False
print(type(a))
print(type(b))


# In[38]:


list=["apple","orange","cherry","banana"]
list2=["monkey","tiger"]
print(list)
print(list[0])
print(list[1:-1])
print(list[2:])
for i in range(0,2):
    print(list)
print(list+list2)


# In[39]:


tuple=("carrot","pomegranate","brinjal","onion")
tuple1=("chilly","tomato")
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tuple*2)
print(tuple+tuple1)


# In[36]:


dict={
    "one":"Bus",
    "Two":"car",
    "Three":"Train"
}
print(dict)
print(dict["one"])
print(dict["Two"])
print(dict.keys())
print(dict.values())


# In[ ]:




