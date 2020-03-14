class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        nums = sorted(nums)
        results = []
        visited = [False] * len(nums)
        self.dfs(nums, 0, [], results, visited)
        return sorted(results)
        
    def dfs(self, nums, idx, subsets, results, visited):
        results.append(subsets[:])
        
        for i in range(idx, len(nums)):
            if visited[i]:
                continue
            if i>0 and nums[i-1]==nums[i] and not visited[i-1]:
                continue
            
            subsets.append(nums[i])
            visited[i] = True
            self.dfs(nums, i+1, subsets, results, visited)
            subsets.pop()
            visited[i] = False
            
        return
    
"""
visited is duplicated??
"""