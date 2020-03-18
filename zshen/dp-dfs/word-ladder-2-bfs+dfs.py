class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):

        K = self.bfs(start, end, dict) 
        res = []
        if end not in dict:
            dict.add(end)
        self.dfs(start, end, [start], dict, K-1, res)

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
        if K == 0 and visited[-1] == end:
            res.append(visited[:])
            return
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == c:
                    continue
                new = word[:i] + c + word[i+1:]
                if new in visited:
                    continue
                
                if new in dict:
                    visited.append(new)
                    self.dfs(new, end, visited, dict, K-1, res)
                    visited.pop()

        return