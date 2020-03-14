class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        
        results = []
        visited = [False] * len(nums)
        self.dfs(nums, [], results, visited)
        return results 
        
    def dfs(self, nums, perm, res, visited):
        if len(perm) == len(nums):
            res.append(perm[:])
            return 
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            visited[i] = True
            perm.append(nums[i])
            self.dfs(nums, perm, res, visited)
            visited[i] = False
            perm.pop()
            
        return
