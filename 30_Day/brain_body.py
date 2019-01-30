#!/usr/bin/env python
# coding: utf-8

# In[111]:


# Dependencies
import matplotlib.pyplot as plt
from sklearn import linear_model
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[112]:


# read data 
data = pd.read_csv('brai.csv')
data


# In[113]:


# selecting data
input_data = data[['Brain']]
target_data = data[['Body']]


# In[114]:


plt.scatter(input_data,target_data,marker='*',color = 'blue')
plt.xlabel('Brain-->')
plt.ylabel('Body-->')
plt.show()


# In[115]:


# Creating the object of Linear Regration model and fit or train the model
model = linear_model.LinearRegression()
model.fit(input_data,target_data)


# ### Now if you want to check the result then use Y=m*x + c formula [m = slop(or gradient) , x = independent variable and c = intercept]

# In[116]:


# to get the intercept
model.intercept_


# In[117]:


# to get the slop
model.coef_


# In[118]:


# Y=     m    *  x  +        c
Y = 0.96649637*0.300+91.00439620740687
Y


# In[119]:


# to see the linear line
plt.scatter(input_data,target_data)
plt.plot(input_data,model.predict(input_data),marker = '*',color = 'blue')
plt.xlabel('Brain-->')
plt.ylabel('Body-->')
plt.show()


# In[ ]:




