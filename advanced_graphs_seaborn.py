import seaborn as sns #advanced graphs, or
# more advanced visually with collaboration of matpotlib
import matplotlib.pyplot as plt

sns.displot([1,2,3,4,5]) #distance chart giving numnber of count variables

plt.show()#displays graph in results sepeartely

sns.violinplot([1,2,3,4,5])#shaped like a violin
plt.show()
'''
df=sns.load_dataset("iris")
print(df)
#sns.displot("iris")
'''
data=sns.load_dataset("iris")

sns.lineplot(x="sepal_length",y="sepal_width",data=data)
plt.show()

#you have to sepearte each graph with plt.show() ex lines '8-9' and '17-18'
