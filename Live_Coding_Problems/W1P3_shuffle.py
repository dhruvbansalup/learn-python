# Write a fn shuffle(l1,l2) that return a list containing of first element in l1 then first of l2 and so on

def shuffle(l1,l2):
    new_list=l1
    for i in range(len(l2)):
        try:
            new_list.insert(2*i+1,l2[i])
        except:
            new_list.append(l2[i])
    return new_list

L1 = eval(input())
L2 = eval(input())
print(shuffle(L1,L2))