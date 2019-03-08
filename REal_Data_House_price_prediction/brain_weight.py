#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[48]:


data


# In[2]:


# Get the data 
data = pd.read_csv('dataset.csv')
x = data['Head Size(cm^3)'].values
y = data['Brain Weight(grams)'].values


# In[59]:


# Visualized the data we have
plt.scatter(x,y,color ='red',label='Data points')
plt.xlabel('Head Size(cm^3)-->',fontsize = 12)
plt.ylabel('Brain Weight(grams)-->',fontsize = 12)
plt.legend()
plt.show()


# In[49]:


# mean on x and y
x_mean = np.mean(x)
y_mean = np.mean(y)

up_part = 0
bt_part = 0

#size of data 
n = len(x)
for i in range(n):
    up_part += (x[i] - x_mean)*(y[i] - y_mean) # first calculate neumerator 
    bt_part += np.square(x[i] - x_mean) # then denoninator

    m = up_part/bt_part # then slop or gradient
    c = y_mean - (m*x_mean) # then cofficient [y=m*x+c => c=y-m*x]
print('m ={} and c ={}'.format(m,c))


# In[36]:


# plot the linear line in the graph
plt.scatter(x,y,color = 'red',label = 'Data points')
model = m*x + c
plt.plot(x,model,color = 'green',label = 'Linear Regression')
plt.scatter(x_mean,y_mean,color='yellow',label='x_mean,y_mean')
plt.xlabel('Head Size(cm^3)')
plt.ylabel('Brain Weight(grams)')
plt.legend()
plt.show()


# In[63]:


# Root Mean Squared Error method to calculate accuracy
root = 0
for i in range(n):
    pred = m*x[i] + c 
    root += np.square(y[i] - pred)
root = np.sqrt(root/n)
print("Model accuracy in  Root Mean Squared Error method is = %.2f "%root)


# In[64]:


# R square method
sum_of_pred = 0
sum_of_total = 0
for i in range(n):
    model_pred = m*x[i] + c
    sum_of_pred += np.square(model_pred - y_mean)
    sum_of_total += np.square(y[i] - y_mean)
r_score = (sum_of_pred/sum_of_total)
print("Model accuracy in R square method is = %.2f" % (r_score*100))


# In[65]:


def new(x):
    return 0.26342933948939945*x + 325.57342104944223


# In[66]:


new_inp = int(input('Enter head size in cm^3: '))
new(new_inp)


# In[67]:


0.26342933948939945*new_inp + 325.57342104944223


# In[ ]:




