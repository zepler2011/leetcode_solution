class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        results = []
        self.dfs(n, 0, 0, [], results)
        return results 
        
    def dfs(self, n, lcnt, rcnt, pare, res):
        
        if len(pare) == 2*n and lcnt==rcnt:
            res.append(''.join(pare))
            return 

        if lcnt < n:
            pare.append('(')
            lcnt += 1 
            self.dfs(n, lcnt, rcnt, pare, res)
            pare.pop()
            lcnt -= 1 
            
        if lcnt >0 and rcnt < n and lcnt > rcnt:
            pare.append(')')
            rcnt += 1 
            self.dfs(n, lcnt, rcnt, pare, res)
            pare.pop()
            rcnt -= 1 
            
        return

"""
TODO: 梳理第二个if 条件
"""