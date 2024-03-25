# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 05:10:24 2024

@author: 14692
"""

#bar graph

import matplotlib.pyplot as plt

cities=['New York', 'Dallas', 'Miami']

population=[10000, 20000, 750000]

plt.bar(cities,population)

plt.show()

plt.barh(cities,population)

plt.show()








