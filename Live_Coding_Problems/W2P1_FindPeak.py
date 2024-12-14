# Write a function Findpeak(L) that accepts a list L of n distinct elements and returns the peak element of the list. A list element is a peak if it is greater than its neighbors. For corner elements, we need to consider only one neighbor. Write an efficient solution of O(logn) complexity. Consider that there is only one peak is in the list, L.


# Sample Input 1

# [5, 10, 20, 15]
# Output

# 20

# Sample Input 2

# [1,2,3,4,5,6,7,8]
# Output

# 8
 


def Findpeak(L):
    def binary_search(low, high):
        mid = (low + high) // 2

        # Check if mid is a peak element
        if (mid == 0 or L[mid] > L[mid - 1]) and (mid == len(L) - 1 or L[mid] > L[mid + 1]):
            return L[mid]

        # Move to the left half if the left neighbor is greater
        if mid > 0 and L[mid - 1] > L[mid]:
            return binary_search(low, mid - 1)

        # Otherwise, move to the right half
        return binary_search(mid + 1, high)

    return binary_search(0, len(L) - 1)
