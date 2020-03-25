class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        f = [[False]*(m+1) for _ in range(n+1)]
        f[0][0] = True
        
        for i in range(1, n+1):
            for j in range(m+1):
                f[i][j] = f[i-1][j]
                w = A[i-1]
                if j >= w:
                    f[i][j] = f[i][j] or f[i-1][j-w]
                    
        for j in range(m, -1, -1):
            if f[n][j]:
                return j 
                
        return 0 