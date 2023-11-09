#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pa
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.model_selection import train_test_split


# In[6]:


import sklearn.naive_bayes


# In[7]:


dataset=pa.read_csv('Iris.csv')
print(dataset.describe())
print(dataset.head())


# In[8]:


X=dataset.iloc[:,[1,2,3,4]].values
y=dataset.iloc[:,-1].values


# In[20]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=0)


# In[10]:


sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.fit_transform(X_test)
classifier=sklearn.naive_bayes.GaussianNB()
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)


# In[11]:


cm=confusion_matrix(y_test,y_pred)
ac=accuracy_score(y_test,y_pred)
print("Confusion Matrix:")
print(cm)
print("Accuracy Score:",ac*100,'%')


# In[17]:


new_data=[[5.1,3.5,1.4,0.2],
          [6.2,3.4,5.4,2.3]]


# In[18]:


predictions=classifier.predict(new_data)


# In[22]:


for prediction in predictions:
    print("Predicted class: ",prediction)


# In[ ]:





# In[ ]:




