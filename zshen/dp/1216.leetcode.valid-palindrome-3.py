"""
leet code: 超时的版本：
"""
class Solution(object):
    def helper(self, s, i, j, k, memo):
        i_,j_ = i,j
        if memo[i][j]>0:
            if memo[i][j] == 1:
                return True
            elif memo[i][j] == 2:
                return False
        while i<j:
            if s[i] == s[j]:
                i+=1
                j-=1
                continue 
            elif k>0:
                return self.helper(s, i+1, j, k-1,memo) or self.helper(s,i,j-1,k-1,memo)
            else:
                # not equal, and have used all 'K' allowance
                memo[i_][j_] = 2
                return False        
        memo[i_][j_] = 1
        return True
    
    def isValidPalindrome(self, s, k):
        n = len(s)
        memo = [[0]*n for _ in range(n)]
        return self.helper(s, 0, len(s)-1, k,memo)

"""
1. [done] add helper 
2. [done] change left, right => i,j 
3. [done] add memo array
"""