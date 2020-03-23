class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        n = len(A)
        f = [-1] * n
        f[0] = A[0] 
        
        for i in range(1, n):
            if f[i-1] > 0:
                f[i] = max(f[i-1]-1, A[i])
            else:
                break

        return f[n-1] > -1 


"""
1. state: f[N] how many steps can meka further. -1 means never reach here
2. transfer: 2 cases:
    2.1 f[i-1] is at least 1, so can reach here.
        f[i] is larger of f[i-1] -1 or A[i]
    2.2 f[i-1] = 0, can never reach here, and on wards
3. init; f[0] = A[0]
4. answer:
    f[N-1] > -1
"""