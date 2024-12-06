# Kruskal's ALgo
def Airport(distance_map):
    edges=[[d,u,v] for u in distance_map.keys() for v,d in distance_map[u]]
    edges=sorted(edges,key=lambda x:x[0])
    
    group={x[1]:x[1] for x in edges}
    group.update({x[2]:x[2] for x in edges})
    
    length=0
    
    for d,u,v in edges:
        if group[u]!=group[v]:
            length+=d
            g=group[u]
            for i in group:
                if group[i]==g:
                    group[i]=group[v]
    
    return length
