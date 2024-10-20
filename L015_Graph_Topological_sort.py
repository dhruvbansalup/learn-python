from numpy import *
from L011_Queue import Queue

# Topological Sort for Adj Matrix - O(n^2)
def toposort(AMat):
    rows,cols=AMat.shape
    indegree={}
    toposortlist=[]

    #Calculate the indegree of each node - O(n^2)
    for c in range(cols):
        indegree[c]=0
        for r in range(rows):
            if AMat[r,c]==1:
                indegree[c]+=1
        
    # O(n^2)
    for i in range(rows):
        #Find the nodes with indegree 0 - O(n)
        j=min([k for k in range(cols) if indegree[k]==0])
        toposortlist.append(j)
        #Update the indegree of the nodes - O(n)
        indegree[j]=indegree[j]-1
        for k in range(cols):
            if AMat[j,k]==1:
                indegree[k]=indegree[k]-1
    
    return toposortlist



# Topological Sort for Adj List - O(m+n)
def toposortList(AList):
    #Initializing  - O(m+n)
    indegree,toposortlist={},[]
    for u in AList.keys():
        indegree[u]=0
    for u in AList.keys():
        for v in AList[u]:
            indegree[v]+=1

    zerodegreeQ=Queue()
    for u in AList.keys():
        if indegree[u]==0:
            zerodegreeQ.enqueue(u)
    
    while not zerodegreeQ.isEmpty():
        j=zerodegreeQ.dequeue()
        toposortlist.append(j)
        indegree[j]=indegree[j]-1
        # Update Indegree of the nodes - O(m)
        for k in AList[j]:
            indegree[k]=indegree[k]-1
            if indegree[k]==0:
                zerodegreeQ.enqueue(k)
    return toposortlist