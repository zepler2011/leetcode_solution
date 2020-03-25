class Solution(object):
    def numSquares(self, m):
        """
        :type n: int
        :rtype: int
        """
        nums = []
        i = 1
        while i*i <=m:
            nums.append(i*i)
            i += 1 
        n = len(nums)
        
        f = [[m]*(m+1) for _ in range(n+1)]
        f[0][0] = 0

        for i in range(1, n+1):
            for j in range(m+1):
                f[i][j] =f[i-1][j]
                w = nums[i-1]
                
                if j>=w:
                    f[i][j] = min(f[i][j], f[i][j-w] + 1)
        
        return f[n][m]