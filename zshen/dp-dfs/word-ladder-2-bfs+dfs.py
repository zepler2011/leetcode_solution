class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):

        dict.add(start)
        dict.add(end)
        K = self.bfs(end, start, dict) 
        res = []
        self.dfs(start, end, set(start), [start], dict, K, res)

        return sorted(res)

    def bfs(self, start, end, dict):
        
        d = {}
        distance = 1 
        d[start] = 0
        currq, nextq = [start],[]

        while currq:
            word = currq.pop(0)
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c is word[i]:
                        continue
                    new = word[:i] + c + word[i+1:]
                    if new not in dict:
                        continue
                    if new in d:
                        continue
                    if new == end:
                        d[new] = distance
                        return d 
                    d[new] = distance
                    nextq.append(new)
                    
            if not currq:
                currq,nextq = nextq,currq
                distance += 1 

        return d


    def dfs(self, word, end, visited, ladder, dict, K, res):
        if K[word] == 0 :
            res.append(ladder[:])
            return
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == c:
                    continue
                new = word[:i] + c + word[i+1:]
                if new in visited:
                    continue
                
                if new not in dict:
                    continue
                
                if new in K and K[new] == K[word] -1 :
                    visited.add(new)
                    ladder.append(new)
                    self.dfs(new, end, visited, ladder, dict, K, res)
                    visited.remove(new)
                    ladder.pop()

        return