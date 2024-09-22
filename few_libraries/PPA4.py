# Perform the following experiment:

# (1) Throw a standard, unbiased, six-sided dice n times.
# (2) Get the frequency of occurrence of the numbers from 1 to 6.
# (3) Convert the frequencies to probabilities.
# (4) Represent the probabilities of obtaining each of the six numbers in the form of a bar plot. You can use plt.bar for this purpose.

# Run this experiment for the following values of 
# n: 10,100,1000,10000,100000,1000000 and note down your observations.


import random
import pandas as pd
import matplotlib.pyplot as plt


def throw_die():
    return random.randint(1,6)

n=100
count={}
for i in range(n):
    trial=throw_die()
    if trial not in count:
        count[trial]=1
    else:
        count[trial]+=1
for key in count.keys():
    count[key]=count[key]/n

x=count.keys()
y=count.values()
plt.bar(x,y, color='skyblue', edgecolor='black')
plt.xlabel('Die Face')
plt.ylabel('Probability')
plt.title(f'Probability Distribution of Rolling a Die ({n} Rolls)')
plt.xticks(range(1, 7))  # Set x-ticks to match die faces
plt.grid(axis='y', linestyle='dotted', alpha=0.7)


plt.show()

