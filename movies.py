# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 07:00:16 2024

@author: 14692
"""
import pandas

from sklearn import tree

from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

import matplotlib.image as pltimg


df=pandas.read_csv("C:\\movies.csv")
print(df)

#changes column data in table
d={'UK':0, 'USA':1, 'N':2, 'Yes':1, 'No':0 }
#verifies changes made
df['Nationality']=df['Nationality'].map(d)

#verifies changes made
df['Go']=df['Go'].map(d)

print(df)


#features

features=['Age','Experience','Rank','Nationality']

x=df[features]
y=df['Go']

print(x) # prints everything but go column

print("00000000000000000000000000000000")

print(y) # prints left over column 'go' only


import pydotplus #library installed this morning 3/25

dtree=DecisionTreeClassifier()
data=dtree.fit(x,y)
data=tree.export_graphviz(dtree,out_file=None,feature_names=features)
graph=pydotplus.graph_from_dot_data(data)
graph.write_png('C:\\decisiontree.png')
img=pltimg.imread('C:\\decisiontree.png')
imgplot=plt.imshow(img)

plt.show()
#decison gtree for true or false



