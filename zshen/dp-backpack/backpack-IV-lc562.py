class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        # write your code here
        n = len(nums)
        m = target
        f = [[0]*(m+1) for _ in range(n+1)]
        f[0][0] = 1 
        
        for i in range(1, n+1):
            for j in range(m+1):
                # not put i-th item in
                f[i][j] = f[i-1][j]
                # put i-th item in:
                w = nums[i-1]
                if j>=w:
                    f[i][j] += f[i][j-w]
                    
        return f[n][m]
        
