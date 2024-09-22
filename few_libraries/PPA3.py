# Consider a file named scores.csv that contains the scores of 25 students in Mathematics and Physics.

# Maths,Physics
# 20,80
# 10,30
# 40,30
# 20,30
# 10,5
# 80,90
# 99,100
# 76,84
# 29,100
# 100,30
# 95,92
# 100,100
# 70,74
# 65,88
# 90,93
# 89,91
# 20,40
# 10,30
# 20,25
# 15,34
# 35,25
# 50,70
# 45,55
# 34,43
# 60,67
# Construct a scatter plot with Mathematics scores on the X-Axis and Physics scores on the Y-Axis. You can use plt.scatter for this purpose. Do you observe anything?

import pandas as pd
import matplotlib.pyplot as plt

scores=pd.read_csv("ppa3_scores.csv")

x=scores["Maths"]
y=scores["Physics"]

plt.scatter(x,y, color="green")
plt.xlabel("Maths")
plt.ylabel("Physics")
plt.title("Plot b/w Maths & Physics Marks")
plt.show()