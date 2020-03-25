class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        
        n = len(A)
        f = [[-1]*(m+1) for _ in range(n+1)]
        f[0][0] = 0

        for i in range(1, n+1):
            for j in range(m+1):
                f[i][j] = f[i-1][j]
                w = A[i-1]
                if j>=w:
                    if f[i-1][j-w] > -1:
                        f[i][j] = max(f[i][j], f[i-1][j-w] + V[i-1])

        return max(f[n])