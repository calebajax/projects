# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 05:38:05 2024

@author: 14692
"""
import pandas as pd
from pandas import Series,DataFrame

import matplotlib.pyplot as plt

import numpy as np
import seaborn as sns

#step 1 load data
import pandas as pd

data_set = pd.read_csv("C:\iphone_purchase_records.csv")
print(data_set.head(1))

x = data_set.iloc[:,:-1].values
print(x)
y = data_set.iloc[:, 3].values
print(y)
print(111111111111111111111111111111111111111111)

#preview data sets

# 0 = no bought iphone
# 1 = purchased iphone

print(data_set.dtypes)
print(111111111111111111111111111111111111111111)
print(data_set.describe())
print(111111111111111111111111111111111111111111)
print(data_set.shape)
print(111111111111111111111111111111111111111111)


from sklearn import preprocessing
#step 2 convert gender to number
from sklearn.preprocessing import LabelEncoder
labelEncoder_gender = LabelEncoder()
x[:,0] = labelEncoder_gender.fit_transform(x[:,0])
# optional - if you want to convert x to float data type
import numpy as np
x = np.vstack(x[:, :]).astype(np.float64) #didn't like me using regular float keyword with imported 'numpy' library
print(x)
# step 3 - split data into training and testing
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=0)

print(22222222222222222222222222222222222222222)


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
print(x_train)
print(111111111111111111111111111111111111111111)

print(x_test)
print(111111111111111111111111111111111111111111)

# Step 5 - Logistic regression classifier
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0, solver="liblinear")
classifier.fit(x_train, y_train)
LogisticRegression(random_state=0, solver='liblinear')
y_pred = classifier.predict(x_test)
# Step 7 - Confusion matrix
from sklearn import metrics
cm = metrics.confusion_matrix(y_test, y_pred)
print(cm)
print(111111111111111111111111111111111111111111)

accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy score:",accuracy)
print(111111111111111111111111111111111111111111)

precision = metrics.precision_score(y_test, y_pred)
print("Precision score:",precision)
print(111111111111111111111111111111111111111111)

recall = metrics.recall_score(y_test, y_pred)
print("Recall score:",recall)













