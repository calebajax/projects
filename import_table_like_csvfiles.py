# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 05:17:58 2024

@author: 14692

dia1=pd.read_csv("C:\diabetes.csv")
print(dia1)
print("fsureee")

iris=pd.read_csv("C:\iris.csv")
print(iris)
print("fsureee")

"""

import pandas as pd


sal=pd.read_csv("C:\salary_data.csv")
print(sal)

print(sal.head())
print(111111111111111111)
print(sal.tail())
print(2222222222222222222)
print(sal.shape)
print(3333333333333333333)
print(sal.info())
print(44444444444444444444)
print(sal.describe())

print(sal['Salary'])#gives salary alone only

print(sal.iloc[1:])#indexing or slicing for tables
print(sal.iloc[:1])
print(sal.iloc[:2])


