"""
leet code: 超时的版本：
"""
class Solution(object):
    def helper(self, s, i, j, k, memo):
        i_,j_ = i,j
        if memo[i][j]:
            return True
        while i<j:
            if s[i] == s[j]:
                i+=1
                j-=1
                continue 
            elif k>0:
                return self.helper(s, i+1, j, k-1,memo) or self.helper(s,i,j-1,k-1,memo)
            else:
                # not equal, and have used all 'K' allowance
                memo[i_][j_] = False
                return False        
        memo[i_][j_] = True
        return True
    
    def isValidPalindrome(self, s, k):
        n = len(s)
        memo = [[False]*n for _ in range(n)]
        return self.helper(s, 0, len(s)-1, k,memo)
		
"""
1. [done] add helper 
2. [done] change left, right => i,j 
3. [done] add memo array
"""