# write a fn expanding(L) that takes a list L as input and return True if difference b/w each adjecent pair is increasing strictly
def expanding(l):

    diff_adj_pair=[]
    for i in range(len(l)-1):
        diff_adj_pair.append(abs(l[i]-l[i+1]))

    for i in range(len(diff_adj_pair)-1):
        if(diff_adj_pair[i]>=diff_adj_pair[i+1]):
            return False
    return True
           

L = eval(input())
print(expanding(L))