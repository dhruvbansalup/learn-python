import random

f=open("human.txt","a")
l=['A','C','T','G']
for i in range(999000):
    r=random.choice(l)
    f.write(str(r))
f.close()