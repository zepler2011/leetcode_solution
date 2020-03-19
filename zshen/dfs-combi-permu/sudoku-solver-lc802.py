class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """
    def solveSudoku(self, board):
        r = [0] * 9
        for i in range(9):
            r[i] = set()
        c = [0] * 9
        for i in range(9):
            c[i] = set()
        b = [[0] * 3  for _ in range(3)]
        for i in range(3):
            for j in range(3):
                b[i][j] = set()
        
        cnt = 81
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    cnt -= 1
                    val = board[i][j]
                    if val not in r[i]:
                        r[i].add(val)
                    if val not in c[j]:
                        c[j].add(val)
                    if val not in b[i//3][j//3]:
                        b[i//3][j//3].add(val)

        self.dfs(board, r, c, b, cnt)
        return
    
    def dfs(self, board, r, c, b, cnt):
        if cnt == 0:
            return True
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    continue
                for d in range(1, 10):
                    if d in r[i] or d in c[j] or d in b[i//3][j//3]:
                        continue

                    r[i].add(d)
                    c[j].add(d)
                    b[i//3][j//3].add(d)
                    board[i][j] = d
                    cnt -= 1
                    if self.dfs(board, r,c,b, cnt):
                        return True
                    board[i][j] = 0
                    cnt += 1
                    r[i].remove(d)
                    c[j].remove(d)
                    b[i//3][j//3].remove(d)
                    
        return False
    
# second try:
class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """
    def solveSudoku(self, board):
        # write your code here
        r = [set() for _ in range(9)]
        c = [set() for _ in range(9)]
        g = [set() for _ in range(9)]

        zeroCnt = 81        # zero cnt
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != 0:
                    zeroCnt -= 1 
                    if val not in r[i]:
                        r[i].add(val)
                    if val not in c[j]:
                        c[i].add(val)
                    if val not in g[i//3 + j//3]:
                        g[i//3+j//3].add(val)
                        
        self.dfs(board, r,c,g, zeroCnt)
        return
    
    def dfs(self, board, r,c,g, cnt):
        if cnt == 0:
            return True 
            
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    continue 
                for d in range(1, 10):
                    if d in r[i] or d in c[j] or d in g[i//3+j//3]:
                        continue 
                    
                    r[i].add(d)
                    c[j].add(d)
                    g[i//3+j//3].add(d)
                    board[i][j] = d 
                    cnt -= 1 
                    if self.dfs(board, r,c,g, cnt):
                        return True 
                    cnt += 1 
                    board[i][j] = 0 
                    r[i].remove(d)
                    c[j].remove(d)
                    g[i//3+j//3].remove(d)
                    
        return False 
        
