class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        results = []
        nums = sorted(list(set(candidates)))
        self.dfs(nums, 0, target, [], results)
        return results

    def dfs(self, nums, s, target, combi, res):
        if s == target:
            res.append(combi[:])
            return
        elif s > target:
            return
        
        for i in range(len(nums)):
            s += nums[i]
            combi.append(nums[i])
            self.dfs(nums[i:], s, target, combi, res)
            s -= nums[i]
            combi.pop()
            
        return 