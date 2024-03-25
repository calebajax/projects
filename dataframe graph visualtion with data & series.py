# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 05:02:50 2024

@author: 14692

vector - one dimensional

matrix - 2 dim
series - 1 dim

pandas - 2 dim (level data struct)

dataframe - 2 dim

"""
import pandas as pd
import matplotlib.pyplot as plt

'''
s1=pd.Series([10,20,30,40,50])

print(s1)
print(type(s1))
print("Number of dimensions")
print(s1.ndim)
#1-dim

df=pd.DataFrame([200,300,400,500])

print(df)
print("Number of dimensions") 
print(df.ndim)
print(type(df))


df=pd.DataFrame([100,200,300,400])
print(df)
print("Number of dimensions") 

print(df.ndim)
print(type(df))

print(df.info())
print(1)
print(df.describe())
print(2)
print(df.shape)
'''
df=pd.DataFrame([[10,20,30,40],
                [7,14,21,28],
                [55,15,6,12],
                [15,3,5,23],
                [5,4,9,12]],
                
                columns=['APPLE','ORANGE','BANANA','PEARS'], #case sensitive
                index=['Basket1','Basket2','Basket3','Basket4','Basket5'])


print(df)
print("\n the minimum value of the fruits")
print(df[['APPLE','ORANGE','BANANA','PEARS']].min()) #case sensitive

print("\n the maximum value of the fruits")
print(df[['APPLE','ORANGE','BANANA','PEARS']].max()) #case sensitive

print("\n the standard deviation value of the fruits")
print(df[['APPLE','ORANGE','BANANA','PEARS']].std()) #case sensitive

print("\n the mean value of the fruits")
print(df[['APPLE','ORANGE','BANANA','PEARS']].mean()) #case sensitive

print("\n the median value of the fruits")
print(df[['APPLE','ORANGE','BANANA','PEARS']].median()) #case sensitive

#get graphical visualizations
plt.hist(df)
plt.show()

#get first 5 values using head
print(df.head())
print(df.head(1))
#get last 5 values using tail
print(df.tail())
print(df.tail(1))

#number of rows/columns
print(df.shape)

#get min/max value
print(df.describe())

print(df.sum()) #adds the rows
print(df.count())#counts

#is it dataframe or series use
print(df.info())







plt.boxplot(df)







plt.show()



