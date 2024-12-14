# Write a Python function findCommonElements(L1, L2) that accepts two integer lists L1 and L2 of same length n and return a list that contains elements that are common to both lists. Write a efficient solution that runs in O(nlogn) or better time.

# L1 contains all distinct integers and L2 contains all distinct integers, but there can be many elements common between L1 and L2.
# Returned list contains all elements that are common to L1 and L2. The elements in the returned list can be in any order.
# For example.

# if L1 = [5, 8, 2] and L2 = [6, 8, 1] then, findCommonElements(L1, L2) should return list [8].

# if L1 = [3, 7, 2, 9, 5] and L2 = [6, 3, 7, 5, 4] then, findCommonElements(L1, L2) should return list [3, 7, 5].


# Do not use Python set built-in function


# Sample input

# [23, 24, 18, 22, 20, 10, 17, 12, 16, 19, 21, 15, 14, 11, 13]
# [23, 22, 33, 24, 31, 21, 20, 26, 30, 29, 25, 27, 28, 34, 32]
# Output

# [20, 21, 22, 23, 24]


def findCommonElements(L1,L2):
    L1=sorted(L1)
    L2=sorted(L2)
    
    def binary_search(l, e):
        start, end = 0, len(l) - 1
        while start <= end:
            mid = (start + end) // 2
            if l[mid] == e:
                return mid
            elif l[mid] > e:
                end = mid - 1
            else:
                start = mid + 1
        return -1

        
    first_index, last_index = -1, -1
    
    # Find the first index of common elements
    for i, element in enumerate(L1):
        if binary_search(L2, element) != -1:
            first_index = i
            break
    
    # If no common elements found, return an empty list
    if first_index == -1:
        return []
    
    # Find the last index of common elements
    for i in range(len(L1) - 1, -1, -1):
        if binary_search(L2, L1[i]) != -1:
            last_index = i
            break
    
    # Return the slice of common elements
    return L1[first_index:last_index + 1]
