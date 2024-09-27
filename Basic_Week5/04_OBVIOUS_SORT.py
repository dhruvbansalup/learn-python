def obvious_sort(l):
    x=[]
    while(len(l)>0):
        mini=l[0]
        for i in range(len(l)):
            if (l[i]<mini):
                mini=l[i]
        x.append(mini)
        l.remove(mini)
    return x

l=[63,324,53,1,4,63]
print(obvious_sort(l))