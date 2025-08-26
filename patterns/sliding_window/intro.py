"""
Given an array, find the average of all contigious subarray of size 'K' in it.
"""

# Brute Force Solution
# Time complexity O(N*K) because the inner for loop is of size of K

# Space Complexity O(N-K+1) 
# Number of elements in result is equivalent length of the window start traversal

def find_avgs_of_subarray_brute_force(K, arr):
    res = []
    _sum = 0.0
    # equivalent to windowStart pointer
    for i in range(len(arr)-K+1):
        # summing everything from windowStart to windowEnd
        for j in range(i, i+K):
            _sum += arr[j]
        res.append(_sum/K) # calculate avg
    return res

# Optimal Solution
# Time Complexity O(N)
# Space Complexity O(N-K+1)

def find_avgs_of_subarray_optimal(K, arr):
    res = []
    sum = 0.0
    windowStart = 0
    # Expand window
    for windowEnd in range(len(arr)):
        sum += arr[windowEnd] # Add element
        #slide the window
        # we don't need to slide if we've not hit the required window size of 'K'
        if windowEnd >= K - 1:
            res.append(sum/K) # calc avg
            sum -= arr[windowStart]
            windowStart += 1
    return res
