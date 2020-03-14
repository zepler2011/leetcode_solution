class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        results = []
        self.dfs(sorted(nums), [], results)
        return sorted(results) 

    def dfs(self, nums, subsets, res):
        res.append(subsets[:])

        for i in range(len(nums)):
            subsets.append(nums[i])
            self.dfs(nums[i+1:], subsets, res)
            subsets.pop()
            
        return

"""
1. use slicing instead of idx:
2. note corner cases
"""