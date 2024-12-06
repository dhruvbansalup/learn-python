def Type_of_heap(A):
    FlagMax=True
    FlagMin=True
    for i in range(len(A)):
        left=(2**i)+1
        right=(2**i)+2
        if left<len(A):
            if A[i]<A[left]:
                FlagMax=False
            if A[i]>A[right]:
                FlagMin=False
        if right<len(A):
            if A[i]<A[right]:
                FlagMax=False
            if A[i]>A[left]:
                FlagMin=False
    if FlagMax:
        return "Max"
    elif FlagMin:
        return "Min"
    else:
        return None