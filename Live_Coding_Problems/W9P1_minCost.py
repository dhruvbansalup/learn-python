# There are N stones, numbered 0,1,2,…,N-1. For each i (0 ≤ i ≤ N-1), the height of Stone i is hi.

# There is a frog who is initially on Stone 0. He will repeat the following action some number of times to reach last stone.

# If the frog is currently on Stone i, can jump to Stone i+1 or Stone i+2. Here, a cost of |hi-hj| is incurred, where j is the stone to land on.

# Find the minimum possible total cost to reach at last stone.

# Write a function minCost(H), where H is a list of heights for N stones. The function returns the minimum possible total cost to reach at last stone.

# Sample Input

# [10, 30, 40, 20]
# Output

# 30
# Explanation

# If we follow the path 0 → 1 → 3, the total cost incurred would be

# ∣10−30∣+∣30−20∣=30.


def minCost(H):
    
    graph=[]
    
    for i in range(len(H)-1):
        graph.append((abs(H[i]-H[i+1]),i,i+1))
        if i==len(H)-2:
            continue
        graph.append((abs(H[i]-H[i+2]),i,i+2))
        
    infinite=float("inf")
    distance=[infinite for i in range(len(H))]
    
    distance[0]=0
    for w,u,v in graph:
        distance[v]=min(distance[v],distance[u]+w)
    
    return distance[-1]
        