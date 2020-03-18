class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """
    def solveSudoku(self, board):
        r = [set()] * 9
        c = [set()] * 9
        b = [[0] * 3  for _ in range(3)]
        for i in range(3):
            for j in range(3):
                b[i][j] = set()
        
        for i in range(9):
            for j in range(9):
                if board[i][j] is not 0:
                    val = board[i][j]
                    if val not in r[i]:
                        r[i].add(val)
                    if val not in c[j]:
                        c[j].add(val)
                    if val not in b[i%3][j%3]:
                        b[i%3][j%3].add(val)

        self.dfs(board, 0, 0, r, c, b)
        return
    
    def dfs(self, board, I, J, r, c, b):
        if I == 9 and J == 9:
            return True
        
        for i in range(I, 9):
            for j in range(J, 9):

                for d in range(1, 10):
                    if board[i][j] != 0:
                        continue
                    if d in r[i] or d in c[j] or d in b[i%3][j%3]:
                        continue

                    r[i].add(d)
                    c[j].add(d)
                    b[i%3][j%3].add(d)
                    board[i][j] = d
                    if self.dfs(board, i, j, r,c,b):
                        return True
                    board[i][j] = 0
                    r[i].remove(d)
                    c[j].remove(d)
                    b[i%3][j%3].remove(d)
                    
            return False