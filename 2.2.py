#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import preprocessing


# In[3]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score


# In[6]:


irisData=load_iris()
X=irisData.data
y=irisData.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)


# In[7]:


Knn=KNeighborsClassifier(n_neighbors=7)
Knn.fit(X_train,y_train)


# In[8]:


y_pred=Knn.predict(X_test)
print(y_pred)


# In[9]:


from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))


# In[12]:


print(accuracy_score(y_test,y_pred)*100)


# In[ ]:




