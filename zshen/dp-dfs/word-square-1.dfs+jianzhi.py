class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        # write your code here
        
        if not words or not words[0]:
            return []
        
        results = []
        visited = set()
        self.dfs(words, [], visited, results)
        return results
    
    def dfs(self, A, square, visited, res):
        n = len(A[0])
        if len(square) == n:
            res.append(list(square))
            return

        for w in A:
            if not self.ispossible(A, w, square, visited):
                continue
            square.append(w)
            visited.add(w)
            self.dfs(A, square, visited, res)
            square.pop()
            visited.remove(w)
                
        return


    def ispossible(self, A, w, square, visited):

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

            if not self.existmatch(A, new_prefix, w, visited):
                return False
                
        return True 

    def existmatch(self, A, prefix, w, visited):
        for a in A:
            if a in visited or a == w:
                continue
            if a.startswith(prefix):
                return True
                
        return False