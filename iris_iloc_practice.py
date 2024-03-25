# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 07:25:30 2024

@author: 14692
"""

import matplotlib.pyplot
import pandas as pd

dt1=pd.read_csv("C:\Iris.csv")

print(dt1)

print(dt1.Id)

print(dt1['Id'])


x=dt1.iloc[1:]
print(x)

x=dt1.iloc[:2]
print(x)


x=dt1.iloc[:4]
print(x)

print(dt1[["Id", "Species"]])







