#!/usr/bin/env python
# coding: utf-8


# Dependencies
import matplotlib.pyplot as plt
from sklearn import linear_model
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')



# read data 
data = pd.read_csv('brai.csv')
data



# selecting data
input_data = data[['Brain']]
target_data = data[['Body']]



plt.scatter(input_data,target_data,marker='*',color = 'blue')
plt.xlabel('Brain-->')
plt.ylabel('Body-->')
plt.show()





# Creating the object of Linear Regration model and fit or train the model
model = linear_model.LinearRegression()
model.fit(input_data,target_data)


# ### Now if you want to check the result then use Y=m*x + c formula [m = slop(or gradient) , x = independent variable and c = intercept]




# to get the intercept
model.intercept_





# to get the slop
model.coef_





# Y=     m    *  x  +        c
Y = 0.96649637*0.300+91.00439620740687
Y



# to see the linear line
plt.scatter(input_data,target_data)
plt.plot(input_data,model.predict(input_data),marker = '*',color = 'blue')
plt.xlabel('Brain-->')
plt.ylabel('Body-->')
plt.show()




