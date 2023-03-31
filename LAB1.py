#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn import datasets


# In[3]:


dir(datasets)


# In[4]:


iris=datasets.load_iris()


# In[5]:


dir(iris)


# In[6]:


iris['feature_names']


# In[7]:


iris['data'][0-5]


# In[8]:


iris['data'][0:5]


# In[9]:


print(iris.data[0])


# In[10]:


iris.data[[5.1,3.5,1.4,0.2]]


# In[11]:


iris.data[[12,26,89,114]]


# In[12]:


n_sample,n_features=iris.data.shape


# In[13]:


print('Number of samples',n_sample)


# In[14]:


diabetes=datasets.load_diabetes()


# In[15]:


dir(diabetes)


# In[16]:


diabetes['feature_names']


# In[17]:


diabetes.data


# In[18]:


diabetes['age']


# In[19]:


import numpy as np
import pandas as pd


# In[20]:


d = {'' : np.random.rand(10),
     'two' : np.random.rand(10)}


# In[21]:


df = pd.DataFrame(d)


# In[22]:


df.plot(style=['o','rx'])


# In[23]:


import matplotlib.pyplot as plt
plt.scatter(df['one'], df['two'])
plt.show() 


# In[24]:


import matplotlib.pyplot as plt
plt.scatter(df['one'], df['two'])
plt.show() 


# In[30]:


x=[row[3]for row in diabetes['data']]


# In[31]:


y=[row[4]for row in diabetes['data']]


# In[32]:


plt.scatter(x,y)


# In[33]:


[row[3]for row in diabetes['data']]


# In[ ]:




