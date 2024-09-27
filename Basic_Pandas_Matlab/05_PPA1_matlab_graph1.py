# Plot the following functions using Matplotlib, each on a separate graph.
# f(x)=3x-4


import matplotlib.pyplot as plt
import math

def f1(x):
    return (3 * x) - 4

x=range(100)
# y=[f1(xi) for xi in x]
y=list(map(f1,x))
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = 3x - 4')

plt.show()

