class Solution:
    """
    @param prices: a list of integers
    @param fee: a integer
    @return: return a integer
    """
    def maxProfit(self, P, fee):
        # write your code here
        n = len(P)
        
        f = [[-sys.maxsize]*2 for _ in range(n+1)]
        f[0][0] = 0
        
        for i in range(1, n+1):
            # continue without stock
            f[i][0] = max(f[i][0], f[i-1][0])
            # or sell today:
            if i > 1:
                f[i][0] = max(f[i][0], f[i-1][1]+P[i-1]-P[i-2]-fee)
            
            # continue with stock:
            if i > 1:
                f[i][1] = max(f[i][1], f[i-1][1]+P[i-1]-P[i-2])
            # or buy today:
            f[i][1] = max(f[i][1], f[i-1][0])

        return f[n][0]


"""
1. f[N][2] := f[N][0] : no stock
              f[N][1] : hold stock
              
2. fang change: 
              f[i][0] = max(f[i-1][0],
                            f[i-1][1] + Pn-1 - Pn-2 - fee)
              f[i][1] = max(f[i-1][1] + Pn-1 - Pn-2,
                            f[i-1][0])
                            
3. chu shi: f[0][0] = 0  # physical meaning
            f[0][1] = -inf
4. da an :  f[0][n]
"""