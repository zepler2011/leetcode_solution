class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, s):
        # write your code here
        
        results = []
        visited = set()
        self.dfs(s, n, [], results, visited)
    
        for num in range(1, n+1):
            if str(num) not in results[0]:
                return num
    
    def dfs(self, s, n, combi, res, visited):
        if len(combi)==n-1 and not s:
            res.append(combi[:])
            return 
        
        if not s or len(combi) >= n:
            return
        
        if s[0] == '0':
            return 
        
        # slice the first
        if s[:1] not in visited:
            combi.append(s[:1])
            visited.add(s[:1])
            self.dfs(s[1:], n, combi, res, visited)
            combi.pop()
            visited.remove(s[:1])
        
        if len(s) > 1 and not s.startswith('00') and int(s[:2])<31 and s[:2] not in visited:
            combi.append(s[:2])
            visited.add(s[:2])
            self.dfs(s[2:], n, combi, res, visited)
            combi.pop()
            visited.remove(s[:2])

        return 