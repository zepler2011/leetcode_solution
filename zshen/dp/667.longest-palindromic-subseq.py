class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        if not s:
            return 0
        
        n = len(s)
        f = [[0]* n for _ in range(n)]

        for i in range(n):
            f[i][i] = 1 
            
        for i in range(n-1):
            if s[i] == s[i+1]:
                f[i][i+1] = 2
            else:
                f[i][i+1] = 1
                
        for l in range(2, n):
            for i in range(0, n - l):
                j = i + l
                if s[i] == s[j]:
                    f[i][j] = max(f[i][j], f[i+1][j-1])
                    f[i][j] += 2
                else:
                    f[i][j] = max(f[i+1][j], f[i][j-1])

        return f[0][n-1]