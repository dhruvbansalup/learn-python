from L011_Queue import Queue

def longestpathlist(AList):
    indegree,lpath={},{}
    for u in AList.keys():
        indegree[u],lpath[u]=0,0
    for u in AList.keys():
        for v in AList[u]:
            indegree[v]+=1
    
    zerodegreequeue=Queue()
    for u in AList.keys():
        if indegree[u]==0:
            zerodegreequeue.enqueue(u)
    
    while (not zerodegreequeue.is_empty()):
        j=zerodegreequeue.dequeue()
        indegree[j]-=1

        for k in AList[j]:
            indegree[k]-=1
          
            lpath[k]=max(lpath[k],lpath[j]+1)

            if indegree[k]==0:
                zerodegreequeue.enqueue(k)
    
    return lpath