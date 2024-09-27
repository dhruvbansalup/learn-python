# Write a Python function histogram(l) that takes as input a list of integers with repetitions and returns a list of pairs as follows :.

# - for each number n that appears in l, there should be exactly one pair (n, r) in the list returned by the function, where r is   the number of repetitions of n in l.
# - the final list should be sorted in ascending order by r, the number of repetitions. For numbers that occur with the same number of repetitions, arrange the pairs in ascending order of the value of the number.

def histogram(l):
    list=[]

    # Making Pairs
    for num in l:
        pair=[num,0] #[num,count]
        for n in l:
            if n==num:
                pair[1]+=1 #increase count
        if tuple(pair) not in list:
            list.append(tuple(pair))
           
    #sorting
    sorted_list=[]
    for i in range(len(list)):
        min=0
        for i_pair in range(len(list)):
            if (list[i_pair][1]<list[min][1]):
                min=i_pair
            elif((list[i_pair][1]==list[min][1])and(list[i_pair][0]<list[min][0])):
                    min=i_pair
        sorted_list.append(list[min])
        list.pop(min)

    return(sorted_list)


#Method 2
def histogram(l):
    result = []
    counted = set()  # To track numbers that we've already processed
    
    # Making Pairs
    for num in l:
        if num not in counted:
            pair = [num, l.count(num)]  # Use l.count() to count occurrences
            result.append(tuple(pair))
            counted.add(num)  # Mark this number as counted
    
    # Sorting by count first, then by number
    sorted_result = sorted(result, key=lambda x: (x[1], x[0]))
    
    return sorted_result
