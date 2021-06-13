##import matplotlib.pyplot as plt
##
##x=[1,2,3,4]
##y=[2,5,2,6]
##z=[3,4,6,2]
##
##plt.figure(figsize=(10,10))
##plt.plot(x,y,'g')
##plt.plot(x,z,'r')
###plt.scatter(x,y)
##plt.xlabel('x axis')
##plt.ylabel('y axis')
##plt.title('sample graph')
##plt.show()
##
##
##plt.figure(figsize=(10,10))
##plt.plot(x,y,'g^')
##plt.scatter(x,z)
##plt.xlabel('x axis')
##plt.ylabel('y axis')
##plt.title('sample graph')
##plt.show()
##
##plt.subplot(1,2,1)
##plt.plot(x,y,'g^')
##plt.title('sample graph')
##
##plt.subplot(1,2,2)
##plt.plot(x,z,'ro')
##
##plt.title('sample graph')
##plt.savefig(r'C:\Users\Rajesh\Desktop\image.png')
##plt.show()
##
##
##a=[2000,2001,2002,2003]
##b=[34,54,27,45]
##plt.bar(a,b,color='r')
##plt.xlabel('year')
##plt.ylabel('boys average')
##plt.title('yearly statistics')
##plt.show()
##
##
##
##a=[2000,2001,2002,2003]
##b=[34,54,27,45]
##plt.barh(a,b)
##plt.xlabel('year')
##plt.ylabel('boys average')
##plt.title('yearly statistics')
##plt.show()
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














































































