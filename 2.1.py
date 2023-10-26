#!/usr/bin/env python
# coding: utf-8

# In[1]:


weather=['sunny','sunny','overcast','rainy','rainy','rainy','overcast','sunny','sunny','rainy','sunny','overcast','overcast','rainy']
temp=['hot','hot','hot','mild','cool','cool','cool','mild','cool','mild','mild','mild','hot','mild']
play=['no','no','yes','yes','yes','no','yes','no','yes','yes','yes','yes','yes','no']


# In[4]:


from sklearn import preprocessing
le=preprocessing.LabelEncoder()
weather_encoded=le.fit_transform(weather)
print(weather_encoded)


# In[5]:


temp_encoded=le.fit_transform(temp)
print(temp_encoded)


# In[6]:


label=le.fit_transform(play)
print(label)


# In[7]:


features=list(zip(weather_encoded,temp_encoded))
print(features)


# In[10]:


from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3)


# In[11]:


model.fit(features,label)
predicted=model.predict([[0,1]])
print(predicted)


# In[ ]:




