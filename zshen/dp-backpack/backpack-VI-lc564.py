class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackVI(self, nums, target):
        # write your code here
        n = target
        f = [0]*(n+1)
        f[0] = 1
        
        for i in range(1, n+1):
            for j in range(len(nums)):
                w = nums[j]
                if i>=w:
                    f[i] += f[i-w]

        return f[n]
