# A tourist wants to travel around India from north to south. He has a policy that he never travels back towards the north. Write a Python function longJourney(AList) to find him a route with which he can visit the maximum number of cities according to his policy, where AList represents a graph of cities and routes between them. Every edge in adjacency list AList is a feasible route between one city to another from north to south. The function should return a list in the order the cities are to be visited to visit maximum cities.

def longJourney(AList):
    def GetIndegree(AList):
        indegree={City:0 for City in AList}
        for city in AList:
            for toCity in AList[city]:
                indegree[toCity]+=1
        return indegree
    indegree=GetIndegree(AList)
    PossibleStartingCity=[city for city in AList if indegree[city]==0] #Cities with indegree 0

    memo = {}
    def getLongestPathforCity(city, AList):
        # returns the longest path from the city in map
        if city in memo:
            return memo[city]
        if city not in AList or not AList[city]:
            return [city]
        PossiblePaths=[]
        for toCity in AList[city]:
            PossiblePaths.append([city]+getLongestPathforCity(toCity, AList))
        
        longest_path = max(PossiblePaths, key=len)
        memo[city] = longest_path
        return longest_path
    
    PossiblePaths=[getLongestPathforCity(city, AList) for city in PossibleStartingCity]
    
    return max(PossiblePaths, key=len)





#Test Case
if __name__=="__main__":
    AList={'Madurai': ['Cochin', 'Kanyakumari'],
    'Vaishali': [],
    'Varanasi': ['Khajuraho', 'Bodhgaya'],
    'Thiruvanandhapuram': ['Kanyakumari'],
    'Udaipur': ['Gir', 'Ajanta'],
    'Rishikesh': ['Delhi'],
    'Shimla': ['Rishikesh'],
    'Bangalore': ['Chennai', 'Madurai'],
    'Agra': ['Ranthambore'],
    'Ellora': ['Aurangabad'],
    'Bodhgaya': ['Kolkatta'],
    'Cochin': ['Thiruvanandhapuram'],
    'Pushkar': ['Udaipur', 'Ranthambore'],
    'Ranthambore': ['Khajuraho'],
    'Gir': [],
    'Aurangabad': ['Mumbai'],
    'Kolkatta': ['Ajanta', 'Bangalore', 'Chennai'],
    'Chennai': ['Madurai'],
    'Sravasti': ['Kushinagar'],
    'Leh': ['Shimla'],
    'Sarnath': ['Varanasi'],
    'Delhi': ['Jaipur', 'Agra', 'Sravasti'],
    'Goa': ['Cochin', 'Bangalore'],
    'Kanyakumari': [],
    'Kushinagar': ['Sarnath', 'Vaishali'],
    'Khajuraho': ['Ajanta'],
    'Jaipur': ['Pushkar'],
    'Mumbai': ['Goa'],
    'Ajanta': ['Ellora', 'Aurangabad']}

    print(longJourney(AList))


    # Output should be: ['Leh', 'Shimla', 'Rishikesh', 'Delhi', 'Sravasti', 'Kushinagar', 'Sarnath', 'Varanasi', 'Bodhgaya', 'Kolkatta', 'Ajanta', 'Ellora', 'Aurangabad', 'Mumbai', 'Goa', 'Bangalore', 'Chennai', 'Madurai', 'Cochin', 'Thiruvanandhapuram', 'Kanyakumari']