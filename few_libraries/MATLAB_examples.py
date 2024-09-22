import matplotlib.pyplot as plt
import numpy as np

x=np.array([2,6,3,11,24,8,8,74])
y=np.array([123,145,156,463,243,234,312,123])

plt.subplot(4,2,1)
plt.scatter(x,y)


plt.subplot(4,2,2)
plt.plot(x,y)


plt.subplot(4,2,3)
plt.bar(x,y)

plt.subplot(4,2,4)

plt.subplot(4,2,6)
plt.barh(x,y)


plt.subplot(4,2,7)
x=np.random.normal(170,20,280)
plt.hist(x)


plt.subplot(4,2,8)
y=np.array([35,25,25,15])
mylabel=["Apple","Bananas","Cherries","Dates"]
plt.pie(y,labels=mylabel,startangle=90)


plt.show()

