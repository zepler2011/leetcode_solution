class Solution(object):
    def removeElement(self, nums, target):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        
        n = len(nums)
        
        left = 0
        right = n-1 
        
        while left < right:
            while nums[left] != target and left < right:
                left += 1
                
            while nums[right] == target and left < right:
                right -= 1
                
            if left >= right:
                break 
            
            if nums[left] == target:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        
        if nums[right] == target:
            return right
        else:
            return right + 1 