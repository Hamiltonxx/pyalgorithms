def xorqueries(arr, queries):
    ans = []
    n = len(arr)
    for i in range(1, n):
        arr[i] ^= arr[i-1]

    for q in queries:
        if q[0] == 0:
            ans.append(arr[q[1]])
        else:
            ans.append(arr[q[1]] ^ arr[q[0]-1])
        
    return ans