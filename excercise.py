#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr1 = np.array([1,2,3])
print(arr1)


# In[2]:


arr1[2]


# In[3]:


arr1[2]=5
arr1


# In[4]:


arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)


# In[6]:


print("The shape is 2 rows and 3 columns:", arr2.shape)


# In[7]:


print(arr2[0][2])
print(arr2[0,2])
print(arr2[0,-1])
print(arr2[-1,0])


# In[8]:


arr3 = np.array(['India','china','USA','Mexico'])
print(arr3)


# In[10]:


arr = np.arange(0,20,2)
print(arr)


# In[11]:


arr = np.linspace(0,10,20)
print(arr)


# In[12]:


arr = np.random.rand(10)
print(arr)
print('\n')
arr = np.random.rand(3,4)
print(arr)


# In[13]:


print(np.full((4,6),10))


# In[14]:


arr = [0,1,2]
print(np.repeat(arr,3))


# In[16]:


arr = [0,1,2]
print(np.tile(arr,3))


# In[17]:


identity_matrix = np.eye(3)
print(identity_matrix)


# In[18]:


identity_matrix = np.identity(3)
print(identity_matrix)


# In[19]:


arr = np.random.rand(5,5)
print(arr)


# In[20]:


print(np.sum(arr,axis=0))


# In[21]:


print(np.sum(arr, axis=1))


# In[22]:


print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))


# In[23]:


arr = np.random.rand(5,5)
print(arr)


# In[24]:


print(np.sort(arr, axis=1))


# In[25]:


arr = np.array([4,5,6,7])


# In[26]:


arr1 = np.append(arr,8)
arr1


# In[27]:


arr2 = np.append(arr, [9,10,11])
print(arr2)


# In[28]:


arr2 = np.array([4,5,6,7,9,10,11])
print(arr2)
print('\n')
arr5 = np.delete(arr2, [1,4])
print(arr5)


# In[29]:


arr1 = np.array([[1,2,3,4], [1,2,3,4]])
arr2 = np.array([[5,6,7,8], [5,6,7,8]])


# In[30]:


cat = np.concatenate((arr1,arr2), axis=0)
print(cat)


# In[31]:


cat = np.concatenate((arr1, arr2), axis=1)
print(cat)


# In[ ]:




