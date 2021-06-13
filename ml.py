import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[2,5,2,6]
z=[3,4,6,2]

plt.figure(figsize=(10,10))
plt.plot(x,y,'g')
plt.plot(x,z,'r')
#plt.scatter(x,y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('sample graph')
plt.show()


plt.figure(figsize=(10,10))
plt.plot(x,y,'g^')
plt.scatter(x,z)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('sample graph')
plt.show()

plt.subplot(1,2,1)
plt.plot(x,y,'g^')
plt.title('sample graph')

plt.subplot(1,2,2)
plt.plot(x,z,'ro')

plt.title('sample graph')
plt.savefig(r'C:\Users\Rajesh\Desktop\image.png')
plt.show()


a=[2000,2001,2002,2003]
b=[34,54,27,45]
plt.bar(a,b,color='r')
plt.xlabel('year')
plt.ylabel('boys average')
plt.title('yearly statistics')
plt.show()



a=[2000,2001,2002,2003]
b=[34,54,27,45]
plt.barh(a,b)
plt.xlabel('year')
plt.ylabel('boys average')
plt.title('yearly statistics')
plt.show()
####import numpy as np
##
####a=["A",'B','C',"D"]
####b=[34,54,27,45]
####c=[45,54,38,55]
####
####index=np.arange(4)
####width=0.30
####
####plt.bar(index,b,width,color='g')
####plt.bar(index+width,c,width,color='r')
####
####plt.xlabel('sections')
####plt.ylabel('average')
####plt.title('boys vs girls')
####plt.xticks(index+width/2,a)
####plt.show()
##
##
####a=["A",'B','C',"D"]
####b=[34,54,27,45]
####c=[45,54,38,55]
####
####index=np.arange(4)
####width=0.30
####
####plt.bar(index,b,width,color='g',label='boys')
####plt.bar(index,c,width,color='r',label='girls',bottom=c)
####
####plt.xlabel('sections')
####plt.ylabel('average')
####plt.title('boys vs girls')
####plt.xticks(index,a)
####plt.legend()
####plt.show()
##
##
####a=["A",'B','C',"D"]
####b=[34,54,27,45]
####plt.pie(b,labels=a)
####plt.title('boys performence')
####plt.legend()
####plt.show()
##
##
####import numpy as np
####x=np.random.rand(1000)
#####x=[2,5,8,4]
####plt.hist(x)
####plt.show()

#import required packages
import pandas as pd


#import dataset
data=pd.read_csv(r'C:\Users\SAI KRISHNA\OneDrive\Desktop')

#understanding about data
#print(data.shape)
#print(data.columns)
#print(data['class'].unique())
#print(data['class'].value_counts())

#preprocessing
x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=6)

#import the algorithm
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=5)

#train the algorithm with data
model.fit(xtrain,ytrain)

#accuracy checking
ypred=model.predict(xtest)
print(ypred)
from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred)*100)


#future prediction
print(model.predict([[4. , 2. , 1.8, 0.8]]))













































































