class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, B, A):
        # write your code here
        n = len(A)
        m = len(B)
        f = [[False] * (m+1) for _ in range(n+1)]
        f[0][0] = True 
        
        for i in range (1, n+1):
            for j in range(m+1):
                if A[i-1] is not '*':
                    if j > 0:
                        if A[i-1] == B[j-1] or A[i-1] is '?':
                            f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = f[i-1][j]
                    if j > 0:
                        f[i][j] = f[i][j] or f[i][j-1]
                    
        return f[n][m]



"""
1. state: f[i][j] = True/False

2. zhuan yi: 
        2.1 A[i-1] not '*':
            f[i][j] = f[i-1][j-1] | A[i-1] == B[j-1] or A[i-1] = '?'

        2.2 A[i-1] is '*':
            f[i][j] = f[i][j-1]     # 匹配多个字符中的一个
            f[i][j] = f[i-1][j]     # 匹配0个字符， 匹配字符减一， 元字符不变

3. init:
        3.1 f[0][0] = True
        3.2 f[0][j] = False
            f[i][0] depends 
            
4. da an: f[n][m]
"""