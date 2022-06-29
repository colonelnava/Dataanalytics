#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[2]:


data1=pd.read_csv('D:/nava/gapminder_full.csv')


# In[3]:


data1


# In[4]:


data1.head()


# In[5]:


print(data1.shape)


# In[6]:


data1.columns


# In[7]:


data1.dtypes


# In[8]:


data1.info()


# In[9]:


country_data=data1['country']
country_data.head()


# In[10]:


country_data.tail()


# In[11]:


subset=data1[['country','continent','year']]
subset.head()


# In[12]:


subset.tail()


# In[13]:


data1.describe(include='all')


# In[14]:


data1.hist(figsize=(10,5))


# In[17]:


sns.boxplot(x="year",y="life_exp",data=data1)


# In[18]:


data1=data1.drop(['year'],axis='columns')
data1.head(5)


# In[21]:


data1=data1.rename(columns={"country" : "Countries"})
data1.head(5)


# In[22]:


duplicate_rows=data1[data1.duplicated()]
print('Number of duplicate rows:',duplicate_rows.shape)


# In[23]:


data1.count()


# In[ ]:




