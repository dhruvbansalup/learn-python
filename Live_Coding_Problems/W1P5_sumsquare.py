# write a fn sumsquare(l) that take a nonempty list of int as input and return list[odd,even] where odd is sum of sq all odd no and even is sum of aq all even

def sumsquare(l):
    sum=[0,0] #[odd,even]
    for i in range(len(l)):
        if (l[i]%2==0):
            sum[1]+=l[i]**2
        else:
            sum[0]+=l[i]**2
    return sum


L = eval(input())
print(sumsquare(L))