class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        n = len(s)
        f = [False] * (n+1)
        f[0] = True
        
        for i in range(1, n+1):
            for j in range(i):
                f[i] = f[j] and s[j:i] in dict
                if f[i]:
                    break 
                
        return f[n]
        
"""
1. state: f[i] := s[0:i-1] can break 
2. fang cheng: f[i] = f[j] AND s[j:i-1] in dict, 0<j<i 
3. chu shi: f[0] = True 
4. answer: f[n]
"""