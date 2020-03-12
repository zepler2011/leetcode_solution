class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        if not words or not words[0]:
            return []
        
        results = []
        self.dfs(words, [], results)
        return results
    
    def dfs(self, A, square, res):
        n = len(A[0])
        if len(square) == n:
            res.append(list(square))
            return

        for w in A:
            if not self.ispossible(A, w, square):
                continue
            square.append(w)
            self.dfs(A, square, res)
            square.pop()
                
        return


    def ispossible(self, A, w, square):

        n = len(square)
        m = len(w)
        
        prefix = ''
        for s in square:
            prefix += s[n]
        if not w.startswith(prefix):
            return False
        
        new_square = square + [w]
        n = len(new_square)
        for j in range(n, m):
            new_prefix = ''
            for s in new_square:        
                new_prefix += s[j]

            if not self.existmatch(A, new_prefix, w):
                return False
                
        return True 

    def existmatch(self, A, prefix, w):
        for a in A:
            if a.startswith(prefix):
                return True                
        return False

"""
TODO:
1. [done] remove 'visited' set
2. 'startswith()' => tire
"""
