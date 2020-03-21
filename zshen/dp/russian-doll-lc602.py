class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, E):
        E.sort()

        n = len(E)
        f = [1] * n

        for i in range(n):
            for j in range(i):
                if E[i][0]>E[j][0] and E[i][1]>E[j][1]:
                    f[i] = max(f[i], f[j]+1)
        return max(f)