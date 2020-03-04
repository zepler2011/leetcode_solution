class Solution:
    """
    @param s: A string
    @return: An integer
    """
    
    def calcPalin(self, s):
        n = len(s)
        isPalin = [[False]*n for _ in range(n)]
        
        for mid in range(n):
            i,j = mid, mid
            while i>=0 and j<n and s[i]==s[j]:
                isPalin[i][j] = True
                i -= 1 
                j += 1
                
            i,j = mid,mid+1 
            while i>=0 and j<n and s[i]==s[j]:
                isPalin[i][j] = True 
                i -= 1 
                j += 1 
                
        return isPalin 
    
    def minCut(self, s):
        # write your code here
        n = len(s)
        f = [sys.maxsize]*(n+1)
        f[0] = 0
        
        palin = self.calcPalin(s)
        for i in range(1, n+1):
            for j in range(i):
                # physical meaning: is the string from j to i-1 palindrome ??
                if palin[j][i-1]:
                    f[i] = min(f[i], f[j] + 1)

        return f[n]-1 


"""
1. state: f[n] # physical meaning: how many partitions of palindrome 
2. fang cheng: f[i] = min(f[j] + 1 | if s[j+1..i] is palin ) 0<=j<i 

3. chu shi: f[0] = 0
4. ans: f[n] - 1 # asked for number of cuts

##
calculate palin:

use two while loops:

ispalin[n][n] = false 

i = j = mid

i,j = mid-1, mid

while i>=0 and j<n:
"""