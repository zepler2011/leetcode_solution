class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        
        results = []
        self.dfs(s, [], results)
        return results
        
    def dfs(self, s, combi, res):
        if not s:
            res.append(combi[:])
            return
        
        combi.append(s[:1])
        self.dfs(s[1:], combi, res)
        combi.pop()
        
        if len(s) > 1:
            combi.append(s[:2])
            self.dfs(s[2:], combi, res)
            combi.pop()
        
        return
        
"""
use slicing

到尾巴才加进去，放 if not s: 条件里面。返回值的物理意义是怎样split string 

不用到尾巴就加进去，，放 if not s: 条件外面。返回值的物理意义是全子集或全组合
    
"""