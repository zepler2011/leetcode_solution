class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        # write your code here
        p2w = {}
        w2p = {}
        words =  teststr.split()
        if len(pattern) != len(words):
            return False
        
        n = len(pattern)
        for i in range(n):
            p = pattern[i]
            w = words[i]
            if p in p2w and p2w[p] != w:
                return False
                
            if w in w2p and w2p[w] != p:
                return False 
                
            if p not in p2w and w not in w2p:
                p2w[p] = w
                w2p[w] = p

        return True 

"""
better naming, and remove the 'res' variable
"""