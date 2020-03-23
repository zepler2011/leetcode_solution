class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0 
        
        n, m = len(grid), len(grid[0]) 
        up = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'E':
                    up[i][j] = 1 
                if i > 0 and grid[i][j] != 'W':
                    up[i][j] += up[i-1][j]
                    
        down = [[0] * m for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(m):
                if grid[i][j] == 'E':
                    down[i][j] = 1
                if i < n-1 and grid[i][j] != 'W':
                    down[i][j] += down[i+1][j]

        left = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'E':
                    left[i][j] = 1
                if j>0 and grid[i][j] != 'W':
                    left[i][j] += left[i][j-1]
        
        right = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m-1, -1, -1):
                if grid[i][j] == 'E':
                    right[i][j] = 1 
                if j<m-1 and grid[i][j] != 'W':
                    right[i][j] += right[i][j+1]

        maxkill = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != '0':
                    continue
                kill = up[i][j] + down[i][j] + left[i][j] + right[i][j]
                maxkill = max(maxkill, kill)

        return maxkill 


"""
1. state f[4][n][m] = cnt  
2. fang cheng: 
    - Up side :
        - f[k][i][j] = 1 | E 
        - f[k][i][j] = 0 | W OR empty
        - f[k][i][j]  += f[k][i-1][j]
3.
4. 
"""