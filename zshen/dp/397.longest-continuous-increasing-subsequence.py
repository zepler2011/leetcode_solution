class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        if not A:
            return 0
            
        n = len(A)
        f1 = [1]*n
        f2 = [1]*n
        
        for i in range(1,n):
            if A[i]>A[i-1]:
                f1[i]+=f1[i-1]

        for i in range(n-2, -1, -1):
            if A[i]>A[i+1]:
                f2[i]+=f2[i+1]

        m1 = max(f1)
        m2 = max(f2)
        return (max(m1,m2))

"""
正序和逆序扫描
分别用打擂台
"""