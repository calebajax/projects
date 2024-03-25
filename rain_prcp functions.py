import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import datetime

data = pd.read_csv("C:\seattleweather.csv")
'''
print(data)
print(1111111111111111111111111111111111111111111111111111)
print(data.columns)
print(1111111111111111111111111111111111111111111111111111)
print(data.shape)
print(1111111111111111111111111111111111111111111111111111)
print(data.describe())
print(1111111111111111111111111111111111111111111111111111)
print(data.info())
'''

'''

finding null values
'''

print("finding null values")
print(data.isna().sum(axis=0))
print(data[pd.isnull(data['PRCP'])])
print(data[pd.isnull(data['RAIN'])])

sns.countplot(data=data, x='RAIN')
#COUNT represents y values
#there are more false values than true n table
print(1111111111111111111111111111111111111111111111111111)
print('mean')
print(data['PRCP'].mean())


#create function for rainfall and precipitationi
def RAIN_INSERTION(cols):
    RAIN=cols[0]
    if pd.isnull(RAIN):
        return 'FALSE'
    else:
        return RAIN
    
def PRCP_INSERTION(col):
    PRCP=col[0]
    if pd.isnull(PRCP):
        return data['PRCP'].mean()
    else:
        return PRCP

#if they have null values false if not will give me the values













