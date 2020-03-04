class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, N):
        # write your code here
        n = len(N)
            
        s = [0]*n
        s[0] = N[0]
        for i in range(1, n):
            s[i] = s[i-1]+N[i]
            
        f = [[-sys.maxsize]*n+1 for _ in range(n)]
        for i in range(n):
            f[i][i] = N[i]
            f[i][n] = S[n-1]-S[i]+N[i]

        for i in range(n):
            for j in range(n):
                if i>=j:
                    continue
                f[i][j] = max(f[i][j-1], s[j]-s[i])
        
        ans = [f[i][n-1] for i in range(n)]
        return max(ans)


"""
1. state: f[n][n] := max sum for sub array A[i..j]
2. fang cheng:  f[i][j] = max(f[i][j-1], f[i][j-1] + A[i][j])

3. 初始 
4. ans: max(f[i][N])

"""