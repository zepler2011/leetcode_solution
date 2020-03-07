class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        results = []
        self.dfs(s, wordDict, 0, [], results)
        return results 
		
    def dfs(self, s, dict, start, candidates, res):
        n = len(s)
        #print start, candidates
        if start == n:
            res.append(' '.join(candidates))
            return
		
        for i in range(start,n+1):
            prefix = s[start:i]
            if prefix not in dict or prefix == '':
                continue
            candidates.append(prefix)
            self.dfs(s, dict, i, candidates, res)
            candidates.pop()
        return