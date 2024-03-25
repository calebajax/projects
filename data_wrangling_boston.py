# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 06:42:25 2024

@author: 14692
"""

import numpy as np
import pandas as pd
boston=pd.read_csv("C:\Boston.csv")
print(boston)
#find dic keys
print(boston.keys())


boston_df=pd.DataFrame(boston)

print(boston_df.shape)
print(boston_df.shape)

print(boston_df.describe())
boston_df.head()
boston_df.boxplot()

import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x=boston_df['dis'])
def outlier_treatment(col):
    sorted(col)
    Q1,Q3 = np.percentile(col , [25,75])
    IQR = Q3 - Q1
    lower_range = Q1 - (1.5 * IQR)
    upper_range = Q3 + (1.5 * IQR)
    return lower_range,upper_range




lower_range,upper_range = outlier_treatment(boston_df['dis'])
#has to be negative
print("Lower Range:",lower_range)
#has to be positive
print("Upper Range:",upper_range)


lower_boston_df = boston_df[boston_df["dis"].values < lower_range]
lower_boston_df

lower_boston_df=boston_df[boston_df["dis"].values < lower_range]
lower_boston_df

upper_boston_df=boston_df[boston_df["dis"].values < lower_range]
upper_boston_df
lower_outliers=lower_boston_df.value_counts().sum(axis=0)
upper_outliers=upper_boston_df.value_counts().sum(axis=0)
total_outliers = lower_outliers + upper_outliers

print("The total number of outliers is: ", total_outliers)

lower_index=list(boston_df[ boston_df["dis"] < lower_range].index)
upper_index=list(boston_df[ boston_df["dis"] < upper_range].index)
total_index=list(lower_index+upper_index)

print("Total index: ")
print(total_index)


print("Shape After Dropping Outlier Rows:", boston_df.shape)
print(boston_df.mean())

%matplotlib inline
sns.boxplot(x=boston_df['dis'])
boston_df.skew(axis=0, skipna=True)
boston_df.skew(axis=0, skipna=True).plot()

#dis variable name for distancd 














