import time

def rbinary_search(L,k,begin,end):
    if(begin==end):
        if (L[begin])==k:
            return 1
        else:
            return 0

    if(end-begin==1):
        if(L[begin]==k) or (L[end]==k):
            return 1
        else:
            return 0
    if (end-begin>1):
        mid=(begin+end)//2
        if (L[mid]>k):
            end=mid-1
        if(L[mid]<k):
            begin=mid+1
        if(L[mid]==k):
            return 1
    if (end-begin<0):
        return 0

    return rbinary_search(L,k,begin,end)
 
L=list(range(100))
k=61

start_time = time.perf_counter()  # Record the start time
result = rbinary_search(L, k,0,len(L))  # Perform the search
end_time = time.perf_counter()  # Record the end time

print(result)  # Print the result of the search
b_time=end_time - start_time
print(f"Binary_search takes: {b_time} seconds")  # Print the time taken
