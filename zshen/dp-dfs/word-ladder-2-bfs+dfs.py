class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):

        K = self.bfs(start, end, dict) 
        visited = set(start)
        res = []
        self.dfs(start, end, visited, dict, K, res)

        return sorted(res)

    def bfs(self, start, end, dict):
        atoz = 'abcdefghijklmnopqrstuvwxyz'
        currq, nextq = [start], []
        visited = set()
        cnt = 1
        
        while currq:
            word = currq.pop(0)
            for i in range(len(word)):
                for new in atoz:
                    if word[i] == new:
                        continue
                    newWord = word[:i] + new + word[i+1:]
                    if newWord in visited:
                        continue
                    if newWord == end:
                        cnt += 1
                        return cnt 
                    elif newWord in dict:
                        nextq.append(newWord)
                        visited.add(newWord)
            if not currq:
                currq,nextq = nextq,currq
                cnt += 1
        
        return cnt        
    

    def dfs(self, word, end, visited, dict, K, res):
        if K == 0:
            return

        for i in range(len(word)):
            for new in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == new:
                    continue
                newWord = word[:i] + new + word[i+1:]

                if newWord in visited:
                    continue
                
                if K == 1 and newWord == end:
                    # need to store
                    res.append(list(visited).append(newWord))
                    return
                
                if newWord in dict:
                    visited.add(newWord)
                    self.dfs(newWord, end, visited, dict, K-1, res)
                    visited.remove(newWord)

        return

"""
1. [done] change 2 queues back to 1 queue, ignore cnt 
2. change the BFS to DFS:
"""