#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import math
from scipy import stats
from scipy.stats import f
import statsmodels.api as sm
from statsmodels.formula.api import ols


# In[2]:


a = [4,3,2]
b = [2,4,6]
c = [2,1,3]


# In[3]:


stats.f_oneway(a,b,c)


# In[4]:


data = pd.read_excel('C:/Users/User/Downloads/oneway.xlsx')


# In[5]:


data


# In[6]:


data_new = pd.melt(data.reset_index(), id_vars=['index'],value_vars=['Teaching Methodology 1','Teaching Methodology 2','Teaching Methodology 3'])
data_new.columns = ['index','Treatments','value']


# In[7]:


data_new


# In[8]:


model = ols('value ~ C(Treatments)',data=data_new).fit()
anova_table = sm.stats.anova_lm(model, typ=1)
anova_table


# In[ ]:




