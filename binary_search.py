import time

def linear_search(L,k):
    for x in L:
        if x==k:
            return 1
    return 0


def binary_search(L,k):
    first=0
    last=len(L)-1

    while ((last-first)>1):
        mid=(first+last)//2
        if(L[mid]==k):
            print(F'Index of {k} in list is: {mid}')
            return
        elif(L[mid]>k):
            last=mid
        else: #L[mid]<k
            first=mid
    if L[first]==k:
        print(F'Index of {k} in list is: {first}')
    elif L[last]==k:
        print(F'Index of {k} in list is: {last}')
    else:
        print(f'{k} is not found')
    return

L=list(range(1000000))
k=50000

start_time = time.perf_counter()  # Record the start time
result = binary_search(L, k)  # Perform the search
end_time = time.perf_counter()  # Record the end time

print(result)  # Print the result of the search
b_time=end_time - start_time
print(f"Binary_search takes: {b_time} seconds")  # Print the time taken


start_time = time.perf_counter()  # Record the start time
result = linear_search(L, k)  # Perform the search
end_time = time.perf_counter()  # Record the end time

print(result)  # Print the result of the search
l_time=end_time - start_time
print(f"Linear_search takes: {l_time} seconds")  # Print the time taken

print(l_time>b_time)