#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import preprocessing


# In[4]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# In[6]:


dataset=pd.read_csv('diabetes.csv')
print(len(dataset))
print(" ")
print(dataset)


# In[36]:


zero_not_accepted=['Glucose','BloodPressure','SkinThickness','BMI','Insulin']
for column in zero_not_accepted:
    dataset[column]=dataset[column].replace(0,np.NaN)
    mean=int(dataset[column].mean(skipna=True))
    dataset[column]=dataset[column].replace(np.NaN,mean)
print(dataset['Glucose'],dataset['BloodPressure'],dataset['SkinThickness'],dataset['BMI'],dataset['Insulin'])


# In[38]:


X=dataset.iloc[:,0:8]
y=dataset.iloc[:,8]
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0,test_size=0.2)
print(len(X_train))
print(len(y_train))
print(len(X_test))
print(len(y_test))


# In[39]:


sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)


# In[40]:


import math
math.sqrt(len(y_test))


# In[41]:


classifier=KNeighborsClassifier(n_neighbors=11,metric='euclidean')


# In[42]:


classifier.fit(X_train,y_train)


# In[43]:


y_pred=classifier.predict(X_test)
print(y_pred)


# In[44]:


print(accuracy_score(y_test,y_pred)*100, '%')


# In[46]:


from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))


# In[ ]:




