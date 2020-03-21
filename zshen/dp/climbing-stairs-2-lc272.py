class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        f = [0] * (n+1)
        f[0] = 1
        
        for i in range(1, n+1):
            f[i] += f[i-1]
            if i > 1:
                f[i] += f[i-2]
            if i > 2:
                f[i] += f[i-3]
                
        return f[n]



"""
1. zhuang tai:   f[N+1] : how many ways 
2. calculate:    f[i] = f[i-1] + f[i-2] + f[i-3]
3. chu shi:      f[0] = 1
            f[1] = f[0] = 1 
            f[2] = f[1] + f[0] = 2
            f[3] = f[2] + f[1] + f[0] = 4 
4 ans:    f[N]
"""