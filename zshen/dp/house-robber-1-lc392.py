class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        n = len(A)
        f = [-sys.maxsize] * (n+1)
        f[0] = 0
        if n>0:
            f[1] = A[0]
        
        for i in range(2, n+1):
            f[i] = max(f[i-1], f[i-2] + A[i-1])
        
        return f[n]



"""
1. ding yi: f[i] = max money of 前i
2. zhuan yi:    f[i] = max(f[i-2] + A[i-1], f[i-1]) 
3. bian jie:    f[0] = 0, f[1] = A[0]
4. da an:       f[n]
"""