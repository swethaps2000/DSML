#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pa


# In[4]:


data=pa.Series([33,5,32,4,333])
data


# In[10]:


data=pa.Series([10,20,30,40,50,60],index=['a','b','c','d','e','f'], dtype='int8')
data


# In[11]:


data.values


# In[13]:


array_data=data.values
print(array_data)


# In[14]:


data.index


# In[22]:


data_series={
            'colum1':pa.Series([50,45,40,35,30,25,20,15,10],dtype='int8'),
            'colum2':pa.Series([10,15,20,25,30,35,40],dtype='int8')
            }
print(data_series)


# In[23]:


pa.DataFrame(data_series)


# In[34]:


movies_df = pa.read_csv('https://raw.githubusercontent.com/ammishra08/MachineLearning/master/Datasets/boston_train.csv', sep = ',')
print(movies_df)


# In[26]:


movies_df.head()


# In[33]:


movies_df.tail()


# In[39]:


pip install openpyxl


# In[42]:


stock_data = pa.read_excel("https://github.com/ammishra08/MachineLearning/raw/master/Datasets/data_akbilgic.xlsx", header=1)


# In[43]:


stock_data


# In[46]:


movies_df.shape


# In[47]:


movies_df.columns


# In[48]:


len(movies_df.columns)


# In[ ]:


print(movies_df.shape[0],movies_df.shape[0])


# In[5]:


data_ser = {
                'Column1' :  pa.Series([100, 200, 300, 400, 500, 600], index = ['a','b','c','d','e','f'], dtype = 'int16'),
                'Column2' :  pa.Series([10, 20, 30, 40, 50, 70], index = ['a','b','c','d','e','g'], dtype = 'int16')
              }
df = pa.DataFrame(data_ser)
df


# In[6]:


df.isnull()


# In[7]:


df.isnull().sum()


# In[8]:


df.isna().sum()


# In[9]:


df.notnull()


# In[10]:


df[df['Column1'].isnull() == True]


# In[11]:


df[df['Column2'].isnull() == True]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




