class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n = len(nums)
        f = [nums[0]]
        for i in range(1, n):
            if nums[i] > f[-1]:
                f.append(nums[i])
            else:
                idx = self.findFirstLargerPosition(f, nums[i])
                f[idx] = nums[i]
                    
        return len(f)
    
    def findFirstLargerPosition(self, array, target):
        # find first position larger than it
        
        start,end = 0,len(array)-1
        
        while start+1<end:
            mid = (start+end)//2
            if target >= array[mid]:
                start = mid 
            elif target < array[mid]:
                end = mid
        
        if array[start] >= target:
            return start 
        elif array[end] >= target:
            return end 
        
        assert('Could not find a position equal to or larger than target', False)
        return