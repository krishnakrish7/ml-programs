import pandas as pd


#import dataset
data=pd.read_csv(r'C:\Users\SAI KRISHNA\OneDrive\Desktop\iris.csv')

#understanding about data
#print(data.shape)
#print(data.columns)
#print(data['class'].unique())
#print(data['class'].value_counts())
#data=data.fillna((0))#this is used to fill the empty spaces in csv file
#print(data.head())#this prints the starting values of data
print(data.isnull())
data=data.fillna((1))
print(data.head())
print(data.tail())



#preprocessing
x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=6)

#import the algorithm
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()

#train the algorithm with data
model.fit(xtrain,ytrain)

#accuracy checking
ypred=model.predict(xtest)
print(ypred)
from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred)*100)


#future prediction
print(model.predict([[4. , 2. , 1.8, 0.8]]))
