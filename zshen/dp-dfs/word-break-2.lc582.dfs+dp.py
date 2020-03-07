class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        results = []
        dp = self.calc(s, wordDict)
        self.dfs(s, wordDict, 0, [], results, dp)
        return results 
		
    def dfs(self, s, dict, start, candidates, res, dp):
        n = len(s)
        if start == n:
            res.append(' '.join(candidates))
            return
		
        for i in range(start,n+1):
            if i<n and not dp[i]:
                continue 
            prefix = s[start:i]
            if prefix not in dict or prefix == '':
                continue
            candidates.append(prefix)
            self.dfs(s, dict, i, candidates, res, dp)
            candidates.pop()
        return

    def calc(self, s, dict):
        # write your code here
        n = len(s)
        f = [False] * (n+1)
        f[0] = True
        
        for i in range(1, n+1):
            for j in range(i):
                f[i] = f[j] and s[j:i] in dict
                if f[i]:
                    break 
                
        return f
"""
1. compare with return value edition 
2. Add DP
3. string slicing
"""