class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, A):
        # write your code here
        n = len(A)
        if n <= 1:
            return n 
            
        f = [[(0,0)]*n for _ in range(n)]
        
        for i in range(n):
            f[i][i] = (1,A[i])
            
        for l in range(1,n):
            for i in range(0, n-l):
                j = i+l
                lis, maxVal = f[i][j-1]
                if A[j] > maxVal:
                    f[i][j] = (lis+1,A[j])
                else:
                    f[i][j] = (lis,maxVal)
        
        for r in f:
            print r 
        ans = [f[i][n-1][0] for i in range(n)]
        return max(ans)
        
        
"""
反例： [10,1,11,2,12,3,11]

"""