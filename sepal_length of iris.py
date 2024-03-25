# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 06:12:41 2024

@author: 14692
"""

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

iris=load_iris()
print(iris)


data=iris.data
sepal_length=data[:,0]
print(sepal_length)

plt.scatter(range(len(sepal_length)),sepal_length,color='g',label='Sepal_Length')
plt.title("Sepal Length of Iris")
plt.xlabel("Iris")
plt.ylabel("sepal length in cm")

plt.legend()
plt.show()

plt.plot(sepal_length)
plt.show()


plt.boxplot(sepal_length)
plt.show()






