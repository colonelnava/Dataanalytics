#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = {'state': ['ohio','ohio','ohio','Nevada','Nevada','Nevada'],'year': [2000,2001,2002,2001,2002,2003],
       'pop': [1.5,1.7,3.6,2.4,2.9,3.2]}
frame = pd.DataFrame(data)
frame


# In[3]:


frame.head()


# In[5]:


frame2 = pd.DataFrame(data, columns=['year','state','pop','debt'],index=['one','two','three','four','five','six'])
frame2


# In[6]:


frame2.columns


# In[7]:


frame2['state']


# In[8]:


frame2.year


# In[9]:


frame2.loc['three']


# In[10]:


frame2['debt']=16.5
frame2


# In[13]:


frame2['debt'] = np.arange(6.)
frame2


# In[14]:


val = pd.Series([-1.2,-1.5,-1.7], index=['two','four','five'])
frame2['debt'] = val
frame2


# In[15]:


frame2['eastern'] = frame2.state == 'ohio'
frame2


# In[16]:


del frame2['eastern']
frame2.columns


# In[18]:


pop = {'Nevada' : {2001: 2.4, 2002: 2.9},'ohio':{2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
frame3


# In[19]:


frame3.T


# In[20]:


pd.DataFrame(pop, index=[2001, 2002, 2003])


# In[21]:


frame3.index.name = 'year'; frame3.columns.name = 'state'
frame3


# In[22]:


frame3.values


# In[23]:


frame2.values


# In[ ]:




