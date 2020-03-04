class Solution:
    """
    @param nums: an array
    @return: the number of longest increasing subsequence
    """
    def findNumberOfLIS(self, A):
        # Write your code here
        n = len(A)
        f = [1]*n
        c = [1]*n
        
        for i in range(n):
            for j in range(i):
                if A[i]>A[j]:
                    if f[i] < f[j]+1:
                        c[i] = c[j]
                    elif f[i] == f[j]+1:
                        c[i] += c[j]
                    f[i] = max(f[i], f[j]+1)
                    
        m = 0
        for i in range(1,n):
            if f[i]>f[m]:
                m = i 
        cnt = 0
        for i in range(n):
            if f[i] == f[m]:
                cnt += c[i]
        return cnt 

"""
1. f[] : 以一个值为结尾的
2. 方程： f[i] = max(f[i-j] + 1) |A[i]>A[j] 0<j<i
          c[i] = c[j] if first time
                 c[j] + c[i] if f[i] == f[j]+1
3. chushi:
   - f[N] = 1 
   - c[N] = 1
4. da an:
        c[k] where f[k] is max
"""