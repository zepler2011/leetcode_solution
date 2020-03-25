class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        # write your code here
        
        n = len(A)
        f = [[-1]*(m+1) for _ in range(n+1)]
        f[0][0] = 0 
        
        for i in range(1, n+1):
            for j in range(m+1):
                # do not use i-th item:
                f[i][j] = f[i-1][j]
                # use i-th item:
                w,v = A[i-1], V[i-1]
                if j>=w and f[i][j-w] > -1:
                    f[i][j] = max(f[i][j], f[i][j-w] + v)
                #XXX below not working, why ???
                #if j>=w and f[i-1][j-w] > -1:
                    #f[i][j] = max(f[i][j], f[i-1][j-w] + v)
                    #k = j 
                    #while k+w < m+1:
                    #    f[i][k+w] = max(f[i][k+w], f[i][k] + v)
                    #    k += w
                        
        return max(f[n])
