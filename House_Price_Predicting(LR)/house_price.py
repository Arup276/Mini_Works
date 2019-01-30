#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
get_ipython().run_line_magic('matplotlib', 'inline')


# In[33]:


# Read the data from csv file
df = pd.read_csv('House.csv')
df


# In[36]:


# Selecting data
input_data = df[['area']]
target_data = df[['price']]


# In[38]:


# Plot the points
plt.scatter(input_data,df.price,marker='*',color = 'blue')
plt.xlabel('Brain-->',fontsize = 15)
plt.ylabel('Body-->',fontsize = 15)
plt.show()


# In[40]:


# create the object and train the model
model = linear_model.LinearRegression()
model.fit(df[['area']],df.price)


# In[42]:


# Now visualize the line
plt.scatter(input_data,df.price,marker='*',color = 'blue')
plt.plot(input_data,model.predict(input_data),color = 'red')
plt.xlabel('Brain-->',fontsize = 15)
plt.ylabel('Body-->',fontsize = 15)
plt.show()


# In[ ]:




