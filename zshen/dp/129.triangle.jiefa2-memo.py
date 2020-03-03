class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, T):
        # write your code here
        if not T or not T[0]:
            return 0
            
        n = len(T)
        memo = [[-sys.maxsize] * n for _ in range(n)]
        return self.calc(0,0,T,memo)


    def calc(self, i, j, T,memo):
        if memo[i][j] > -sys.maxsize:
            return memo[i][j]
            
        if i == len(T)-1:
            memo[i][j] = T[i][j]
            return T[i][j]
        
        s = T[i][j]   
        left = self.calc(i+1, j, T,memo)
        right = self.calc(i+1, j+1, T,memo)
        s += min(left,right)
        memo[i][j] = s
        return s 

"""
解法一：分治/divide and conque。分别计算下面两个值，然后求小的
    超时，加入一个memo数组来记录是否计算过，可以过

"""