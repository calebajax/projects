# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 05:57:13 2024

@author: 14692
"""

import matplotlib.pyplot as plt

ages=[22,30,42,56,85,92]

plt.boxplot(ages)

plt.show()

plt.boxplot(ages,showmeans=True)
plt.show()
#prints grean triangle to display mean