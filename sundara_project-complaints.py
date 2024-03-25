# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 06:44:17 2024

@author: 14692
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.decomposition import FactorAnalysis, PCA

import random
from datetime import datetime as dt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import PolynomialFeatures

from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler,OneHotEncoder
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split

from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
df = pd.read_csv("C:\Comcast Telecom Complaints data.csv")
print(df)
date_array1 = []
date_array =df['Date'].values
len1 = len(date_array)
print(len1)

print('---------------------------------------------')

df = df.drop_duplicates()
print(df)
print('---------------------------------------------')

df1 = df.describe()
print(df1)

#uniqueness
for column in df.columns:
    
    distinct_value=len(df[column].unique())
    print(f'{column}: {distinct_value} distinct values')
#===========================================

sns.countplot(x ='Received Via', data = df)

complaints_by_Month = df['Ticket #'].values

monthc = np.array(df['Ticket #'].index)

# June has maximum complaints. When the temperature turns warm, comcast has problems with connectivity
plt.plot( monthc, complaints_by_Month) 
plt.title("Comcast Monthly Complaints") 
plt.xlabel('Month')
plt.ylabel('Complaint count') 
plt.show() 

# June has maximum complaints. When the temperature turns warm, comcast has problems with connectivity
plt.plot( monthc, complaints_by_Month) 
plt.title("Comcast Monthly Complaints") 
plt.xlabel('Month')
plt.ylabel('Complaint count') 
plt.show() 

plt.scatter( monthc, complaints_by_Month) 
plt.title("Comcast Monthly Complaints")
plt.xlabel('Month')
plt.ylabel('Complaint count')
 
plt.show()

print('-----------------------------------------')

#3 Frequency of major complaints
complaints =  [df['Customer Complaint'].values]

carray = []
for i in range(0,2224):
    carray.append(complaints[0][i])
  
complaints =  [df['Customer Complaint'].values]

carray = []
for i in range(0,2224):
    carray.append(complaints[0][i])
#carray    
darray = []
farray = []
for i in range(0,2224):
    
    darray.append(carray[i].split())

#darray[0]
for i in range(0,2224):
    
    farray = farray + darray[i]
len1 = len(farray)
for i in range(0,len1):
    
    farray[i] = farray[i].lower()

print(len(farray))
farray = [x  for x in farray if (len(x) > 4) ]
len1 = len(farray)
#farray = [x  for x in farray if not (x[0].isnumeric)  ]

sdf = pd.DataFrame({'larray':farray})
sdf = sdf.drop_duplicates()
len2 =len(sdf)
narray = sdf['larray'].values
print(len2)





