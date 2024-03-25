import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

heart1=pd.read_csv("C:\heart_download.csv")


print(heart1)
print(heart1.shape)
print(heart1.info())
print(heart1.describe())


#find unque values or columns

for column in heart1.columns:
    uniquevalues=len(heart1[column].unique())
    print("The unique values are, ",uniquevalues)
    
#find duplicate values
duplicates=heart1[heart1.duplicated()]  
print("number of duplicated rows is, ",duplicates) 
# comes up as result at end of isplayed dupicated data:
#                               [723 rows x 14 columns]
    

heart1=heart1.drop_duplicates()
print(heart1)
#result when duplicates dropped after displayed data
#                           [302 rows x 14 columns]

#plot graph age
#plt.hist(heart1['age'])
plt.hist(heart1['age'],bins=10,color='blue',edgecolor='yellow')
plt.title('Age of Distribution')
plt.xlabel('age')
plt.ylabel('frequency')

plt.show

count=heart1['sex'].value_counts()

#graph information                #calculates percentages of male to female
plt.pie(count,labels=count.index, autopct='%1.2f%%')
plt.title("male 2 female distubution")
plt.show()

plt.boxplot(heart1['trestbps'])
plt.title('resting presure distribution')
plt.ylabel('resting blood pressure (mm hg')
plt.show()

import seaborn as sns #can plot the counts

sns.countplot(x='cp',data=heart1)

plt.title("chest pain types")
plt.xlabel('chest pain')
plt.ylabel('count')
plt.show()

plt.scatter(heart1['age'],heart1['thalach'],color='purple')

plt.title('Age vs Maximum Heart Rate Achieved')
plt.xlabel('age')                 
plt.ylabel("Maximum Heart Rate Achieved")                   
plt.show()

#the more the plot the better the output
#have to decide how to graph data given the set of information


#data science is visusalization
                  
                   