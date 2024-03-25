# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 05:18:24 2024

@author: 14692
"""

import matplotlib.pyplot as plt

import numpy as np

y=np.array([10,20,30,40])

plt.pie(y)#default color
plt.show()

y=np.array([10,20,30,40])
c=['r','g','y','b']
plt.pie(y,colors=c)
plt.show

y=np.array([10,20,30,40])
cities=['New York','Tokoyo','Dallas','Houston']
c=['r','g','y','b']
plt.pie(y,colors=c,labels=cities)
plt.show



