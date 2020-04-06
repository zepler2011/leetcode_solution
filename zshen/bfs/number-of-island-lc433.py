class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        n,m = len(grid), len(grid[0])
        visited = set()
        queue = []
        cnt = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "0":
                    continue
                if (i,j) in visited:
                    continue 
                cnt += 1    
                queue.append((i,j))
                visited.add((i,j))
                while queue:
                    (x,y) = queue.pop(0)
                    for dx,dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                        x_ = dx+x
                        y_ = dy+y
                        if x_>=0 and x_<n and y_>=0 and y_<m and grid[x_][y_]=="1" and (x_,y_) not in visited:
                            queue.append((x_,y_))
                            visited.add((x_,y_))
                            
        return cnt 