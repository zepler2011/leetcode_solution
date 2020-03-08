class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        # write your code here
        d = {}
        d2 = {}
        words =  teststr.split()
        res = []
        if len(pattern) != len(words):
            return False
        
        n = len(pattern)
        for i in range(n):
            c = pattern[i]
            w = words[i]
            if c not in d:
                if w in d2:
                    return False
                d[c] = w
                d2[w] = c
            res.append(d[c])
            
        for i in range(n):
            if res[i] != words[i]:
                return False
            
        return True 

"""
'values' must be unique
"""