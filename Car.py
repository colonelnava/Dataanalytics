#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy.optimize import minimize
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


import pandas as pd
tbl = pd.read_excel('C:/Users/User/Downloads/regcar.xlsx')
tbl


# In[4]:


import statsmodels.api as sm
x= tbl['TV Ads']
y=tbl['car Sold']
x2 = sm.add_constant(x)
modl = sm.OLS(y,x2)
modl2 = modl.fit()
print(modl2.summary())


# In[5]:


e=modl2.resid


# In[6]:


e


# In[7]:


np.std(e)


# In[13]:


def lik(parameters):
    m = parameters[0]
    b = parameters[1]
    sigma = parameters[2]
    for i in np.arange(0, len(x)):
        y_exp = m * x + b
    L = (len(x)/2 * np.log(2 * np.pi) + len(x)/2 * np.log(sigma ** 2) + 1 / (2 * sigma ** 2) * sum((y - y_exp) ** 2))
    return L    


# In[14]:


lik_model = minimize(lik, np.array([5,5,5]), method='Nelder-Mead')


# In[15]:


lik_model.x


# In[16]:


plt.scatter(x,y)
plt.plot(x, lik_model['x'][0] * x + lik_model['x'][1])
plt.show()


# In[ ]:




