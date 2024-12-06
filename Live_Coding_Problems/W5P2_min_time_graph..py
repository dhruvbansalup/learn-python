# You are given a network of n nodes, labelled from 0 to n-1. You are also given travel_times, a list of signal travel times in as directed edges travel_times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# Write a function min_transmission_time(n, travel_times, s) that accept number of nodes n, a list travel_times and a source node s to send the signal . The function returns the minimum time required for the signal sent by the source node s to be received by all the remaining n-1 nodes. If it is impossible to obtain a signal for all n-1 nodes, return -1.

def min_transmission_time(n,travel_times,s):
  
    infinite=float('inf')
    time={x:infinite for x in range(n)}
    
    time[s]=0
    
    for _ in range(n-1):
        for (u,v,w) in travel_times:
            if time[u]<infinite:
                time[v]=min(time[v],time[u]+w)
            
    if any(t == infinite for t in time.values()):
        return -1
    
    return max(time.values())