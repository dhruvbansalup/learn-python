import time
def linear_search(L,k):
    for x in L:
        if x==k:
            return 1
    return 0



L = list(range(100))  # Create a large list for testing

start_time = time.perf_counter()  # Record the start time
result = linear_search(L, 5)  # Perform the search
end_time = time.perf_counter()  # Record the end time

print(result)  # Print the result of the search
print(f"Time taken: {end_time - start_time} seconds")  # Print the time taken