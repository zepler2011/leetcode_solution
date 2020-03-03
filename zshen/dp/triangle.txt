class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, A):
        # write your code here
        if not A or not A[0]:
            return None 
            
        n = len(A)
        f = [[-sys.maxsize] * n for _ in range(n)]
        for i in range(n):
            f[n-1][i] = A[n-1][i]
            
        for i in range(n-2, -1, -1):
            for j in range(n):
                if i<j:
                    continue 
                f[i][j] = min(f[i+1][j], f[i+1][j+1]) + A[i][j]
                
        return f[0][0]


"""
1. state:   f[N][N] := min number:
2. zhuan yi:  f[i][j] = min(f[i+1][j], f[i+1][j+1]) + A[i][j]
3. bian jie:  f[i][N] = A[i][N]
4. da an:     f[0][0]

计算顺序：从大到小
"""

