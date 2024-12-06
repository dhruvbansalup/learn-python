# Cool Worker

# A group of workers have to complete a list of tasks, those tasks have dependencies within the task list. But the workers prefer some interesting task and hates to do some boring task. They always do the most interesting one among the available tasks to be done.

# Write a function coolworkers(AList, preference) to return the order in which the tasks will be  done. AList is the adjacency list with the dependencies and preference is the tasks sorted in preferred order, in which task in index 0 is the most preferred and index-1 (last element) be the least preferred.



def coolWorkers(AList,preference):
    indegree={x:0 for x in AList.keys()}
    result=[]
    for i in AList.keys():
        for j in AList[i]:
            indegree[j]+=1
    
    #Get task with indegree 0
    Q=[x for x in indegree.keys() if indegree[x]==0]
    
    def prefered(list,preference):
        for task in preference:
            if task in list:
                return task
    
    while len(Q)!=0:
        j=prefered(Q,preference)
        result.append(j)
        Q.remove(j)
        
        indegree[j]-=1
        for k in AList[j]:
            indegree[k]-=1
            if indegree[k]==0:
                Q.append(k)
    return result





# Test Case
AList = {0: [1, 2, 3],
1: [7],
2: [3, 5],
3: [4, 1, 8],
7: [],
5: [6, 1],
4: [5, 7],
8: [5],
6: [7]}
preference = [1, 3, 2, 6, 8, 5, 4, 0, 7]
print(coolWorkers(AList, preference))
# Output:  [0, 2, 3, 8, 4, 5, 1, 6, 7]
