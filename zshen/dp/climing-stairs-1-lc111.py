class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        
        if n < 2:
            return n
            
        f = [0]* (n+1)
        f[0] = 1 
        
        for i in range(1, n+1):
            f[i] += f[i-1]
            if i > 1:
                f[i] += f[i-2]
                
        return f[n]


"""
1. f[n+1]
2. f[i] = f[i-1] + f[i-2]
3. chu shi: f[0]=1 
4. ans: f[n]
"""