# Write a function findRedundantEdges(E,n) that accept an edge list E in increasing order of the edge weight where all edge weights are distinct and the number of vertices n (labeled from 0 to n-1) in a connected undirected graph and the function returns a list of redundant edges in increasing order of weight, so by removing these edges, the graph should remain connected with the minimum total cost of edges(minimum cost spanning tree). Try to write solution code of complexity O((E+V)logV).

# Note - Selected edges tuples in the output list should be similar to input list edges tuples.

# Hint- Union-find data structure



def findRedundantEdges(edges,n):
    visited={x:0 for x in range(n)}
    group={x:x for x in range(n)}

    extra_edges=[]

    for (u,v,w) in edges:
        if group[u]!=group[v]:
            visited[u],visited[v]=True,True
            g= group[u]
            for i in group:
                if group[i]==g:
                    group[i]=group[v]
        else:
            extra_edges.append((u,v,w))
    
    return extra_edges


#Test Case 1
n = 4
E=[(0,1,10),(1,2,20),(2,3,30),(3,0,40),(1,3,50)]
print(findRedundantEdges(E,n))
# Output
# [(3, 0, 40), (1, 3, 50)]

#Test Case 2
n = 7
E=[(0,1,10),(0,2,50),(0,3,60),(5,6,75),(2,1,80),(6,4,90),(1,6,100),(2,5,110),(1,3,150),(3,4,180),(2,4,200)]
print(findRedundantEdges(E,n))
# Output
# [(2, 1, 80), (2, 5, 110), (1, 3, 150), (3, 4, 180), (2, 4, 200)]