class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """
    def isPalin(self,s, left, right):
        #left,right = 0,len(s)-1 
        while left<right and s[left]==s[right]:
            left+=1 
            right-=1 
        return left>=right 
    
    def validPalindrome(self, s):
        left,right=0,len(s)-1
        
        while left<right:
            if s[left] == s[right]:
                left += 1 
                right -= 1
                continue 
            else:
                # 另一种写法，string slicing 但是右边界是下标+1
                #return self.isPalin(s, left+1, right) or self.isPalin(s, left,right-1)
                return self.isPalin(s, left+1, right) or self.isPalin(s, left,right-1)
        return True 
    
    
    def wrong_validPalindrome(self, s):
        # Write your code here
        n = len(s)
        left = 0
        right = n-1
        allow = 1 
        
        while left<right:
            if s[left] == s[right]:
                left += 1 
                right -= 1 
                continue 
            elif allow>0:
                if s[left+1] == right:
                    allow -= 1 
                    left += 2
                    right -= 1
                    continue 
                elif s[left] == s[right-1]:
                    allow -= 1 
                    left += 1
                    right -= 2 
                    continue 
            return False 
            
        return True 
		
"""
我的错误答案：
* 原因：没有写出 OR 的关系

修改：
* 改成recursion
"""