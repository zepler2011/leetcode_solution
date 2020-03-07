class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        memo = {}
        return self.dfs(s, wordDict, memo)
        
    def dfs(self, s, dict, memo ):
        if s in memo:
            return memo[s]
        
        partition = []
        n = len(s)
        for i in range(1,n): # skip empty substring
            if s[:i] not in dict:
                continue
            
            prefix = s[:i]
            sub_partition = self.dfs(s[i:], dict, memo)
            for p in sub_partition:
                partition.append(prefix + " " + p)
    
        if s in dict:
            partition.append(s)
            
        memo[s] = partition
        return partition 
     
"""
TODO: 1. pass partition as an argument;
"""
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
        for r in results:
            print r
        return results 

    def dfs(self, s, dict, start, candidates, res):
        n = len(s)
        print start, n, candidates 
        if start == n-1:
            res.append(candidates)
            return

        for i in range(start,n):
            prefix = s[start:i+1]
            print prefix 
            if prefix not in dict:
                continue
            candidates.append(prefix)
            self.dfs(s, dict, start+i, candidates, res)
            candidates.pop()
        return