class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # write your code here
        
        if not grid or not grid[0]:
            return -1 
            
        n,m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        today,tomorrow = [],[]
        infect = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    visited[i][j] = True 
                    today.append((i,j))
                if grid[i][j] == 2:
                    visited[i][j] = True
                if grid[i][j] == 0:
                    infect += 1
        
        days = 1
        while today:
            i,j = today.pop(0)
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                x = i + dx
                y = j + dy 
                if x>=0 and x<n and y>=0 and y<m and not visited[x][y]:
                    tomorrow.append((x,y))
                    visited[x][y] = True 
                    infect -= 1
                    if infect == 0:
                        return days
                    
            if not today:
                today, tomorrow = tomorrow, today
                days += 1 
                
        return -1