# Write a Python function combinationSort(strList) that takes a list of unique strings strList as an argument, where each string is a combination of a letter from a to z and a number from 0 to 99, the initial character in string being the letter. For example a23, d5, q99 are some strings in this format. This function should sorts the list and return two lists (L1, L2) in the order mentioned below.

# L1: First list should contain all strings sorted in ascending order with respect to the first character only. All strings with same initial character should be in the same order as in the original list.

# L2 : In the list L1 above, sort the strings starting with same character, in descending order with respect to the number formed by the remaining characters.

def combinationSort(strList:list):
    def insert_char(l:list,v:str,sortNum:bool):
        inserted=False
        for i in range(len(l)):
            if l[i][0]==v[0] and sortNum:
                if int(l[i][1:])<int(v[1:]):
                    l.insert(i,v)
                    inserted=True
                    break
            elif l[i][0]>v[0]:
                l.insert(i,v)
                inserted=True
                break
        if not inserted:
            l.append(v)
        return l
    
    L1=[]
    L2=[]
    for item in strList:
        insert_char(L1,item,0)
        insert_char(L2,item,1)
    return(L1,L2)


print(combinationSort(('d34','g54','d12','b87','g1','c65','g40','g5','d77')))
print(combinationSort(('a23', 'a5', 'a99')))