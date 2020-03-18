class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, A, B):

        m = len(A)
        n = len(B)
        f = [[False] * (m+1) for _ in range(n+1)]
        
        f[0][0] = True
        for i in range(1, m+1):
            f[0][i] = False
            
        for i in range(1, n+1):
            for j in range(m+1):
                if B[i-1] is not '*':
                    if j > 0:
                        if A[j-1] == B[i-1] or B[i-1] is '.':
                            f[i][j] = f[i-1][j-1]
                else:
                    if i > 1:
                        f[i][j] = f[i-2][j]
                        
                        if B[i-2] is '.' or B[i-2] == A[j-1]:
                            f[i][j] = f[i][j] or f[i][j-1]
        
        #for r in f:
        #    print r
                            
        return f[n][m]

        

"""
1. state: f : true or false 
2. fang cheng: 
// 我的A B 和讲解中是反着的：
    2.1 if B[i-1] is not *:
        f[i][j] = f[i-1][j-1] | A[j-1] == B[i-1] OR B[i-1] == '.'
    
    2.2 if B[i-1] is * :
    
    i > 2:
        f[i][j] = f[i-2][j]     # physical meaning c* not match anything in A 
        OR 
        # c* matches a char in string A 
        f[i][j] = f[i][j-1] | B[i-2] == '.' OR A[j-1] == B[i-2]

3. Init: 
    f[0][0] = True 
    f[0][j] = False     # 空pattern 不match anything string 
    f[i][0]  depends    # 空串有可能match，也可能不match

4. 答案：
    f[n][m]
"""