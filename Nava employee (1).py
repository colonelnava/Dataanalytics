#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/User/Downloads/employees.csv")
print(df.head())


# In[ ]:





# In[3]:


print(df.dtypes)
print(df.describe())


# In[4]:


print('Salary')
print(df['Salary'].head(10))


# In[5]:


print(df['Gender'].head(10))


# In[6]:


missing_value_formats = ["n.a.","?","NA","n/a","na","--"]
df = pd.read_csv("employees.csv", na_values = missing_value_formats)

print(df['Gender'].head(10))


# In[7]:


missing_value_formats = ["n.a.","?","NA","n/a","na", "--"]
df = pd.read_csv("C:/Users/User/Downloads/employees.csv", na_values = missing_value_formats)

print(df['Gender'].head(10))


# In[9]:


import pandas as pd
missing_value_formats = ["n.a.","?","NA","n/a","na", "--"]
df = pd.read_csv("C:/Users/User/Downloads/employees.csv", na_values = missing_value_formats)

def make_int(i):
    try:
        return int(i)
    except:
        return pd.np.nan
    
df['Salary'] = df['Salary'].map(make_int)
print(df['Salary'].head())


# In[10]:


print(df['Gender'].isnull().head(10))
print(df['Gender'].notnull().head(10))  


# In[11]:


null_filter = df['Gender'].notnull()
print(df[null_filter].head())


# In[12]:


print(df.isnull().values.any())


# In[13]:


print(df.isnull().sum())


# In[14]:


new_df = df.dropna(axis = 0, how = 'any')
print(new_df)


# In[15]:


new_df = df.dropna(axis = 0,how = 'all')
print(new_df)


# In[16]:


new_df = df.dropna(axis = 1, how ='any')
print(new_df)


# In[17]:


new_df = df.dropna(axis = 1,how = 'all')
print(new_df)


# In[19]:


df['Salary'].fillna(0)


# In[20]:


df['Gender'].fillno('No Gender')


# In[21]:


df['Gender'].fillna('No Gender')


# In[22]:


df['Salary'].fillna(method='pad')


# In[23]:


df['salary'].fillna(methods = 'bfill')


# In[24]:


df['salary'].fillna(method = 'bfill')


# In[26]:


df['Salary'].fillna(method = 'bfill')


# In[27]:


df['Salary'].fillna(df['Salary'].median())


# In[28]:


df['Salary'].fillna(int(df['Salary'].mean()))


# In[29]:


df['Salary'].replace(to_replace = np.nan, value = 0)


# In[30]:


df['Salary'].interpolate(method='linear',direction = 'forward')


# In[ ]:




