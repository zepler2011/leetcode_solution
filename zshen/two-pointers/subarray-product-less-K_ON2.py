    def numSubarrayProductLessThanK(self, nums, k):
        # Write your code here
        if not nums:
            return 0
        
        n = len(nums)
        product = [0] * (n+1) 
        p = nums[0]
        product[1] = nums[0]
        
        for i in range(2, n+1):
            p *= nums[i-1]
            product[i] = p 
            
        cnt = 0
        for i in range(1, n+1):
            p = product[i]
            if p<k:
                cnt += i
            else:
                j = 1
                while j<i and p/product[j] >= k:
                    j += 1
                cnt += i-j
        
        return cnt