# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 05:50:04 2024

@author: 14692
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
# Read the CSV File:
data = pd.read_csv("C:\FuelConsumption.csv")
print(data)




#scatter plot good to use to compare two data values, or like see the correlation between the two
data.head()

data = data[["ENGINESIZE", "CO2EMISSIONS"]]
#enginesize vs co2emissions
plt.scatter(data["ENGINESIZE"], data["CO2EMISSIONS"], color='green')
plt.xlabel("ENGINESIZE")
plt.ylabel("CO2EMISSIONS")
plt.show()

#Generating training and testing data from our data:
    # we are using %80 data for training
    #80* =: before int

train = data[:(int((len(data)*0.8)))]
print(train)


#20* test =int(len():) -: after
test = data[(int((len(data)*0.8))):]
# it becomes .20 when you put the semicolon after the line of code because that is what's ;eft of .80
# so if i had .90 and ':' is at the end it would be .10 left
# if i had .70 and ':' after .3 is left

# Using sklearn package to model data :
regr = linear_model.LinearRegression()
train_x = np.array(train[["ENGINESIZE"]])
train_y = np.array(train[["CO2EMISSIONS"]])
regr.fit(train_x,train_y)
# The coefficients:
print ("coefficients : ",regr.coef_) #Slope
print ("Intercept : ",regr.intercept_) #Intercept
# Plotting the regression line:
plt.scatter(train["ENGINESIZE"], train["CO2EMISSIONS"], color='blue')
plt.plot(train_x, regr.coef_*train_x + regr.intercept_, '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")

#linear regression scatter plot get for testing the upside downside
#ex
#-jobs in america going up and down
# - the US dollar with inflation
#- population of a demographic in an area overtime 

