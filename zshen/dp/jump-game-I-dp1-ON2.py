class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        n = len(A)
        f = [False] * n
        f[0] = True 
        
        for i in range(1, n):
            for j in range(i):
                if f[j] and A[j] >= i-j:
                    f[i] = True
                    break
                
        return f[n-1]


"""
1. state: f[N+1] True or false 
2. transfer: 
    f[i] =  True | f[j]=True AND A[j-1] >= i-j for 0<=j<i;
    // 枚举j from 0 to i
3. init; f[0] = True, f[1] = True 
4. answer:
    f[N]
"""