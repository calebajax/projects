# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt

a=[10,20,30,40,56]
b=[1,3,5,7,9]
#plt.plot(a)<-- 

plt.title("rainfall")

plt.xlabel("rainfaill in mm")

plt.ylabel("temp")


plt.plot(a,b,'g',marker='o')
plt.plot(a,b,'ro') #dotted line graph
#plt.plot(a,b,"r") straightline

plt.show()


#------------------------------------
plt.plot(a,b,'g',marker='o')

plt.show()

plt.plot(a,b,'g',marker='o')

plt.show()

plt.plot(a,b,'g',marker='d',markersize=10)


"""
view-->panes-->plot = see graph given coded info above

"""



