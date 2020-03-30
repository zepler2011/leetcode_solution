class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        # Write your code here
        results = []
        self.dfs(s, 0, 0, [], results)
        return results 

    def dfs(self, s, lcnt, rcnt, path, res):
        if not s:
            res.append(''.join(path))
            return 
        
        if self.paren_is_valid(s[0], lcnt, rcnt):
            path.append(s[0])
            if s[0] == '(':
                valid = self.dfs(s[1:], lcnt+1, rcnt, path, res)
            elif s[0] == ')':
                valid = self.dfs(s[1:], lcnt, rcnt+1, path, res)
            else:
                valid = self.dfs(s[1:], lcnt, rcnt, path, res)
            if valid:
                return
            path.pop()
            
        if len(s) > 1 and self.paren_is_valid(s[1], lcnt, rcnt):
            path.append(s[1])
            if s[1] == '(':
                valid = self.dfs(s[2:], lcnt+1, rcnt, path, res)
            elif s[1] == ')':
                valid = self.dfs(s[2:], lcnt, rcnt+1, path, res)
            else:
                valid = self.dfs(s[2:], lcnt, rcnt, path, res)
            if valid:
                return 
            path.pop()
            
        return 
    
    def paren_is_valid(self, c, l, r):
        if c == '(':
            return l+1 >= r 
        elif c == ')':
            return l >= r+1
        
        return True