class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, A):
        # write your code here
        if not A:
            return 0
        
        n = len(A)
        f = [1] * n
        t = [-1] * n
        maxLen = 1
        maxIdx = 0
        for i in range(n):
            for j in range(i):
                if A[i] > A[j]:
                    if f[j]+1 > f[i]:
                        f[i]=f[j]+1
                        t[i]=j
                    if f[i] > maxLen:
                        maxLen = f[i]
                        maxIdx = i
        res = []
        while maxIdx > -1:
            res.append(A[maxIdx])
            maxIdx = t[maxIdx]
        print res
        return maxLen 

        
"""
例： [10,1,11,2,12,3,11]

f[i] physical meaning:
 - the subsequence ends in A[i], regardless of what it contains.
 - Then there are two scenarios:
    1. exists an element A[j], A[i]>A[j]. So f[i]=f[j]+1
    2. A[j] is smallest, then f[i] = 1

"""