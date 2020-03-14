class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        nums = [i for i in range(1, n+1)]
        results = []
        self.dfs(nums, [], results, k)
        return results

    def dfs(self, nums, combi, res, k):
        if len(combi)==k:
            res.append(combi[:])
            return

        for i in range(len(nums)):
            combi.append(nums[i])
            self.dfs(nums[i+1:], combi, res, k)
            combi.pop()

        return 
    
"""
use slicing:
    - 不用去重，不用visited
"""