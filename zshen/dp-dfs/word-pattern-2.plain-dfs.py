class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, P, s):
        # write your code here
        self.p2s = {}
        self.s2p = {}
        
        res = []
        self.dfs(s, P, 0, [], res)
        
        return len(res) > 0


    def dfs(self, s, P, start, candidate, res):
        n = len(s)
        # reached end of pattern and string
        if start == n and not P:
            res.append(list(candidate))
            return
            
        m = len(P)
        for i in range(m):
            c = P[i]
            newP = P[i+1:]
            for j in range(start+1, n+1):
                # make current value for the key 'c'
                word = s[start:j]

                # key exist
                if c in self.p2s and word != self.p2s[c]:
                    continue
                # word exist, but not match
                if word in self.s2p and c != self.s2p[word]:
                    continue
                if c not in self.p2s and word not in self.s2p:
                    self.p2s[c] = word 
                    self.s2p[word] = c
                    # done with above, now can continue:
                    candidate.append(word)
                    self.dfs(s, newP, j, candidate, res)
                    candidate.pop()
                    del self.p2s[c]
                    del self.s2p[word]
                else:
                    candidate.append(word)
                    self.dfs(s, newP, j, candidate, res)
                    candidate.pop()
                
        return
            
"""
2. [done] exit condition
1. [done] in for loop, continue's condition check
    * 四种情况表示两个集合可能的所有4个相交
3. [done] two hashtables need backtracking too
    * 虽然写的不好看，但是逻辑上说的通；

"""