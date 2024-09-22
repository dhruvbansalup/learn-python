#total marks of topper using filehandling
f=open("Scores.csv",'r')
f.readline()

max=-1
for line in f.readlines():
    line=line.strip().split(",")
    
    if int(line[8])>max:
        max=int(line[8])
print(max)


