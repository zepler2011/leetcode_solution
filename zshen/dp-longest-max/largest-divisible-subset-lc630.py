class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largestDivisibleSubset(self, nums):
        # write your code here
        if not nums:
            return []
        
        n = len(nums)
        nums.sort()

        f = [1]*n 
        t = [-1]*n 
        maxLen = 1
        maxIdx = 0
        
        for i in range(1, n):
            for j in range(i):
                if nums[i]%nums[j]==0:
                    if f[j]+1 > f[i]:
                        f[i]=f[j]+1
                        t[i]=j
                    if f[i]>maxLen:
                        maxLen=f[i]
                        maxIdx=i 
        
        res = []
        while maxIdx>-1:
            res.append(nums[maxIdx])
            maxIdx=t[maxIdx]
            
        return sorted(res, reverse=True)
