class Solution:
    """
    @param prices: a list of integers
    @return: return a integer
    """

    def maxProfit(self, A):
        n = len(A)
        f = [[-sys.maxsize] * 2 for _ in range(n+1)]
        f[0][0] = 0
        
        for i in range(1, n+1):
            # continue without stock
            f[i][0] = max(f[i][0], f[i-1][0])
            # sell today
            if i > 1:
                f[i][0] = max(f[i][0], f[i-1][1] + A[i-1]-A[i-2])
            
            if i > 1:
                # continue with stock
                f[i][1] = max(f[i][1], f[i-1][1] + A[i-1]-A[i-2])
            if i > 1:
                # buy today
                f[i][1] = max(f[i][1], f[i-2][0])
            if i == 1:
                # special case, the first "buy" doesn't need cooldown
                f[i][1] = max(f[i][1], f[i-1][0])

        return f[n][0]


"""
无限多次，只需要两个数组分别记录有股票和没有股票即可。一个特例：第一次买不需要cooldown
1. zhuang tai:
2. fang cheng: f[i][0] = max(f[i-1][0], 
                             f[i-1][1] + Pi-1 - Pi-2)
                f[i][1] = max(f[i-1][1] + Pi-1 - Pi-2 ,
                              f[i-2][0])
3. chu shi:   f[0][0] = 0
              f[0][1] = -inf
4. da an:  f[0][n]
"""