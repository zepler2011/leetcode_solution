class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, A):
        # write your code here
        if not A:
            return 0
            
        n = len(A)
        if n == 1:
            return A[n-1]
            
        f = [-sys.maxsize] * (n+1)
        if n > 0:
            f[0] = 0
            f[1] = A[0]
            
        for i in range(2, n):
            f[i] = max(f[i-1], f[i-2]+A[i-1])
            
        money = f[n-1]
        
        f = [-sys.maxsize] * (n+1)
        if n > 1:
            f[0] = 0
            f[1] = 0
            f[2] = A[1]
            
        for i in range(3, n+1):
            f[i] = max(f[i-1], f[i-2] + A[i-1])
            
        money = max(money, f[n])
        
        return money
