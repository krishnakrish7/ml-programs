

#import required packages
import pandas as pd


#import dataset
cnames=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD',
        'TAX','PTRATIO','B','LSTAT','MEDV']
data=pd.read_csv(r'C:\Users\SAI KRISHNA\OneDrive\Desktop\machine learning programs\boston.csv',names=cnames)

#print(data.head())

#print(data.isnull().sum())
data=data.dropna()

x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=4)


#import the algorithm
from sklearn.linear_model import LinearRegression
model=LinearRegression()


#train the algorithm with data
model.fit(xtrain,ytrain)

#error checking
ypred=model.predict(xtest)
#print(ypred)



from sklearn.metrics import mean_squared_error
import math
print(math.sqrt(mean_squared_error(ytest,ypred)))


#future prediction
print(model.predict([[0.09378,	12.5,	7.87,	0,
                      0.524,	5.889,	39,	5.4509,	5,
                      311,	15.2,	390.5,	15.71,]]))



































#import required packages
import pandas as pd


#import dataset
cnames=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD',
        'TAX','PTRATIO','B','LSTAT','MEDV']
data=pd.read_csv(r'C:\Users\SAI KRISHNA\OneDrive\Desktop\machine learning programs\boston.csv',names=cnames)

#print(data.head())

#print(data.isnull().sum())
data=data.dropna()

x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=4)


#import the algorithm
from sklearn.linear_model import LinearRegression
model=LinearRegression()


#train the algorithm with data
model.fit(xtrain,ytrain)

#error checking
ypred=model.predict(xtest)
#print(ypred)



from sklearn.metrics import mean_squared_error
import math
print(math.sqrt(mean_squared_error(ytest,ypred)))


#future prediction
print(model.predict([[0.09378,	12.5,	7.87,	0,
                      0.524,	5.889,	39,	5.4509,	5,
                      311,	15.2,	390.5,	15.71,]]))
































































#import required packages
import pandas as pd


#import dataset
cnames=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD',
        'TAX','PTRATIO','B','LSTAT','MEDV']
data=pd.read_csv(r'C:\Users\SAI KRISHNA\OneDrive\Desktop\machine learning programs\boston.csv',names=cnames)

#print(data.head())

#print(data.isnull().sum())
data=data.dropna()

x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=4)


#import the algorithm
from sklearn.linear_model import LinearRegression
model=LinearRegression()


#train the algorithm with data
model.fit(xtrain,ytrain)

#error checking
ypred=model.predict(xtest)
#print(ypred)



from sklearn.metrics import mean_squared_error
import math
print(math.sqrt(mean_squared_error(ytest,ypred)))


#future prediction
print(model.predict([[0.09378,	12.5,	7.87,	0,
                      0.524,	5.889,	39,	5.4509,	5,
                      311,	15.2,	390.5,	15.71,]]))




























































#import required packages
import pandas as pd


#import dataset

data=pd.read_csv(r'C:\Users\SAI KRISHNA\OneDrive\Desktop\machine learning programs\forestfires.csv')
#print(data.head())

#print(data.isnull().sum())
data=data.drop(['month','day'],axis=1)

x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=6)


#import the algorithm
from sklearn.linear_model import LinearRegression
model=LinearRegression()


#train the algorithm with data
model.fit(xtrain,ytrain)

#error checking
ypred=model.predict(xtest)
#print(ypred)



from sklearn.metrics import mean_squared_error
import math
print(math.sqrt(mean_squared_error(ytest,ypred)))
















































